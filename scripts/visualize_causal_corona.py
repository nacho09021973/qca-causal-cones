"""Generate a self-contained geometric viewer; run from the repository root.

Known: s4 cyclic report (2026-11-06), tetrahedral unit vertices, c_IR=1/3;
ir-corona.tex sections 2 and 4, CJWW cube [-1,1]^3 and c_IR=1.
Question: how does the emergent cone sit inside the microscopic causal body?
Stop: inconsistent vertex lengths, face distances, or directional radial bounds.
This illustrates those recorded geometries only. No wave evolution, photon
trajectories, probabilities, strict-support theorem or new gate calculation.
Uses only the Python standard library; the HTML needs no network or packages.
"""

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

HTML = r'''<!doctype html>
<html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cono, soporte y corona · QCA</title>
<style>
:root{color-scheme:dark;font:15px system-ui,sans-serif;background:#0b111b;color:#e8edf4}
*{box-sizing:border-box}body{margin:0}header,footer{padding:22px 30px}header{border-bottom:1px solid #263247}
h1{font-size:25px;letter-spacing:-.6px;margin:4px 0 8px}p{line-height:1.5;margin:8px 0;color:#abb9ca}
.eyebrow{color:#56d9d0;text-transform:uppercase;letter-spacing:2px;font-size:11px}
.controls{display:flex;gap:16px;align-items:center;flex-wrap:wrap;padding:16px 30px;border-bottom:1px solid #263247}
select,button{background:#182336;color:#f1f5fb;border:1px solid #40516b;border-radius:7px;padding:9px 12px;font:inherit;cursor:pointer}
button:focus-visible,select:focus-visible,input:focus-visible{outline:2px solid #61dfd5}
input{accent-color:#56d9d0}label{display:flex;gap:8px;align-items:center}.layout{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:1px;background:#263247}
.stage,.side{background:#0b111b}.stage{position:relative;min-width:0}#space{width:100%;height:620px;display:block;touch-action:none;cursor:grab}
.badge{position:absolute;top:20px;left:24px;pointer-events:none;font-size:12px;color:#bccbdd}.side{padding:22px}h2{font-size:16px;margin:0 0 12px}
#cone{width:100%;height:300px;display:block}.legend{display:grid;gap:10px;margin:20px 0}.key{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:9px}
.cyan{background:#56d9d0}.amber{background:#ffb65d}.wire{background:#8ea6c8}.note{font-size:12px;line-height:1.6;color:#a2b1c6}.stat{font-size:29px;color:#ffb65d;margin:12px 0}.small{font-size:12px}
footer{border-top:1px solid #263247;font-size:12px;max-width:1100px}.source{color:#7890ae;overflow-wrap:anywhere}
@media(max-width:850px){.layout{grid-template-columns:1fr}#space{height:460px}.side{display:grid;grid-template-columns:1fr 1fr;gap:16px}#cone{height:260px}header,.controls,footer{padding:16px}}
</style>
<header><div class="eyebrow">Geometría causal · visor local</div><h1>El cono no llena todo el soporte</h1>
<p>Una esfera emergente dentro de un cuerpo microscópico. La región entre ambos es la corona geométrica.</p></header>
<div class="controls"><select id="model" aria-label="Modelo"><option value="tetra">s=4 cíclico · tetraedro</option><option value="cube">CJWW · cubo</option></select>
<button id="play">Pausar</button><label>Tiempo <input id="time" type="range" min="0" max="1" step="0.001" value="0.72"><output id="tvalue"></output></label>
<label><input id="dots" type="checkbox" checked>Puntos</label><label><input id="layers" type="checkbox" checked>Capas anteriores</label>
<label><input id="surfaces" type="checkbox" checked>Superficies</label>
<label>Opacidad <input id="opacity" aria-label="Opacidad de las superficies" type="range" min="0.04" max="0.5" step="0.01" value="0.18"></label>
<button id="reset">Recentrar</button><button id="save">Guardar PNG 3D</button></div>
<main class="layout"><section class="stage"><canvas id="space" aria-label="Vista espacial 3D del soporte y la esfera emergente"></canvas>
<div class="badge">SECCIÓN ESPACIAL A TIEMPO t<br>Arrastra para girar · rueda para ampliar</div></section>
<aside class="side"><div><h2>Un corte del cono</h2><label class="small">Dirección <select id="direction"><option value="vertex">Hacia un vértice</option><option value="face">Normal a una cara</option><option value="axis">Eje x</option></select></label>
<canvas id="cone" aria-label="Corte radio-tiempo del cono emergente y la frontera microscópica"></canvas></div>
<div><div class="legend"><span><i class="key cyan"></i>Radio emergente: c_IR · t</span><span><i class="key amber"></i>Corona geométrica</span><span><i class="key wire"></i>Frontera microscópica: t C_micro</span></div>
<div class="small">Anchura de corona en la dirección elegida</div><div class="stat" id="gap"></div>
<p class="note" id="explain"></p><p class="note">Los puntos luminosos son marcadores geométricos de rayos. Su cantidad, brillo y velocidad dibujada no son probabilidades ni trayectorias físicas de fotones. La corona muestra posiciones permitidas por la geometría; no certifica ocupación ni señal.</p></div></aside></main>
<footer><b>Qué se está viendo.</b> El panel 3D muestra tres coordenadas espaciales. Las superficies translúcidas son las dos fronteras de la corona: esfera interior turquesa y poliedro exterior ámbar. La corona es el volumen entre ambas; los puntos interiores no se unen en una malla arbitraria. El panel derecho añade el tiempo en un corte radial: la esfera se convierte en un cono y el cuerpo microscópico genera una frontera exterior. Los rayos se detienen al volver a t=0.
<p>En CJWW, la corona geométrica coincide con la región entre el cubo y la bola del manuscrito. Una señal operacional requiere además el protocolo de preparación, codificación y lectura. En s=4, el visor usa la geometría de un paso y la pendiente local registradas; no identifica el cuerpo asintótico estricto.</p>
<div id="source" class="source"></div></footer>
<script>
const DATA=__DATA__;
const $=id=>document.getElementById(id),canvas=$('space'),ctx=canvas.getContext('2d'),cone=$('cone'),cc=cone.getContext('2d');
let kind='tetra',t=.72,running=true,yaw=.72,pitch=.38,zoom=1,last=0,drag=null;
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),mul=(a,s)=>a.map(x=>x*s),norm=a=>Math.sqrt(dot(a,a));
const model=()=>DATA.models[kind];
function radial(n){return kind==='cube'?1/Math.max(...n.map(Math.abs)):1/Math.max(...model().vertices.map(v=>-3*dot(v,n)));}
function direction(){let d=$('direction').value;return d==='axis'?[1,0,0]:d==='face'?(kind==='cube'?[1,0,0]:mul(model().vertices[0],-1)):(kind==='cube'?[1/Math.sqrt(3),1/Math.sqrt(3),1/Math.sqrt(3)]:model().vertices[0]);}
function fit(c){let b=c.getBoundingClientRect(),d=devicePixelRatio||1;c.width=Math.round(b.width*d);c.height=Math.round(b.height*d);let x=c.getContext('2d');x.setTransform(d,0,0,d,0,0);return [b.width,b.height];}
let sw,sh,cw,ch;
function resize(){[sw,sh]=fit(canvas);[cw,ch]=fit(cone);draw();}
function project(v){let a=Math.cos(yaw),b=Math.sin(yaw),c=Math.cos(pitch),d=Math.sin(pitch);let x=a*v[0]-b*v[1],y=b*v[0]+a*v[1];return [sw*.5+x*sw*.25*zoom,sh*.55-(c*v[2]-d*y)*sw*.25*zoom,c*y+d*v[2]];}
function line(points,color,width=1){ctx.beginPath();points.forEach((v,i)=>{let p=project(v);i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]);});ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();}
function body(scale,alpha){let m=model(),v=m.vertices.map(x=>mul(x,scale));m.edges.forEach(e=>line([v[e[0]],v[e[1]]],`rgba(142,166,200,${alpha})`,1.2));}
function sphere(r){for(let j=0;j<3;j++){for(let lat of [-.65,0,.65]){let path=[];for(let i=0;i<=96;i++){let a=i*Math.PI/48,v=[r*Math.sqrt(1-lat*lat)*Math.cos(a),r*Math.sqrt(1-lat*lat)*Math.sin(a),r*lat];path.push(j===0?v:j===1?[v[2],v[0],v[1]]:[v[1],v[2],v[0]]);}line(path,'rgba(86,217,208,.32)');}}}
// Closed triangulated unit sphere; the poles have one triangle per sector.
const sphereMesh=[];
function spherePoint(i,j){let a=Math.PI*i/18,b=2*Math.PI*j/32;return [Math.sin(a)*Math.cos(b),Math.sin(a)*Math.sin(b),Math.cos(a)];}
for(let i=0;i<18;i++)for(let j=0;j<32;j++){
 const a=spherePoint(i,j),b=spherePoint(i,j+1),c=spherePoint(i+1,j),d=spherePoint(i+1,j+1);
 if(i>0)sphereMesh.push([a,b,c]);if(i<17)sphereMesh.push([b,d,c]);
}
function surfaces(){if(t===0)return;let m=model(),alpha=+$('opacity').value;
 const triangles=sphereMesh.map(tri=>({vertices:tri.map(v=>mul(v,m.c*t)),rgb:'86,217,208'}));
 for(const face of m.faces)for(let i=1;i<face.length-1;i++)
  triangles.push({vertices:[face[0],face[i],face[i+1]].map(k=>mul(m.vertices[k],t)),rgb:'255,182,93'});
 // Painter's order is recalculated on every camera rotation for both boundaries.
 triangles.map(tri=>({...tri,points:tri.vertices.map(project)}))
 .sort((a,b)=>a.points.reduce((s,p)=>s+p[2],0)-b.points.reduce((s,p)=>s+p[2],0))
 .forEach(tri=>{ctx.beginPath();tri.points.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();ctx.fillStyle=`rgba(${tri.rgb},${alpha})`;ctx.fill();});
}
const dirs=Array.from({length:200},(_,i)=>{let z=1-2*(i+.5)/200,a=i*Math.PI*(3-Math.sqrt(5));return [Math.sqrt(1-z*z)*Math.cos(a),Math.sqrt(1-z*z)*Math.sin(a),z];});
function draw(){let m=model();ctx.clearRect(0,0,sw,sh);let grad=ctx.createRadialGradient(sw/2,sh/2,0,sw/2,sh/2,sw*.6);grad.addColorStop(0,'#152338');grad.addColorStop(1,'#0b111b');ctx.fillStyle=grad;ctx.fillRect(0,0,sw,sh);
// Parallel time slices are spatial homotheties, not extra tetrahedral species.
if($('layers').checked)[.25,.5,.75].forEach(q=>body(t*q,.12));
if($('surfaces').checked)surfaces();
body(t,.65);sphere(m.c*t);
[[1,0,0],[0,1,0],[0,0,1]].forEach((n,i)=>{line([mul(n,-1.18),mul(n,1.35)],'#283c55');let p=project(mul(n,1.4));ctx.fillStyle='#7189a8';ctx.fillText('xyz'[i],p[0],p[1]);});
if($('dots').checked){let dots=[];dirs.forEach((n,i)=>{let end=radial(n),phase=(i*.61803398875)%1;
// Cyan markers lie on the emergent wavefront; amber markers sample the corona.
let speed=m.c+(end-m.c)*(.15+.8*phase);dots.push({p:mul(n,m.c*t),color:'#56d9d0',radius:1.9});
if(end-m.c>1e-8)dots.push({p:mul(n,speed*t),color:'#ffb65d',radius:1.7});});
dots.sort((a,b)=>project(a.p)[2]-project(b.p)[2]).forEach(d=>{let p=project(d.p);ctx.globalAlpha=.45+.5*(p[2]+1.8)/3.6;ctx.fillStyle=d.color;ctx.shadowBlur=7;ctx.shadowColor=d.color;ctx.beginPath();ctx.arc(p[0],p[1],d.radius,0,2*Math.PI);ctx.fill();});ctx.globalAlpha=1;ctx.shadowBlur=0;}
ctx.fillStyle='#d6e1f0';ctx.font='13px system-ui';ctx.fillText(m.name,24,sh-42);ctx.fillStyle='#8199b8';ctx.fillText(`c_IR = ${kind==='tetra'?'1/3':'1'} · t = ${t.toFixed(2)} (unidades de paso)`,24,sh-22);
drawCone();$('tvalue').value=t.toFixed(2);$('time').value=t;$('source').textContent='Fuentes locales: '+m.sources.join(' · ');$('explain').textContent=m.explain;
}
function drawCone(){cc.clearRect(0,0,cw,ch);let R=radial(direction()),c=model().c,X=36,Y=ch-35,W=cw-50,H=ch-62,top=Math.max(1,R)*1.1;let pt=(r,time)=>[X+r/top*W,Y-time*H];
function path(points,fill,stroke){cc.beginPath();points.forEach(([r,time],i)=>{let p=pt(r,time);i?cc.lineTo(...p):cc.moveTo(...p);});if(fill){cc.closePath();cc.fillStyle=fill;cc.fill();}if(stroke){cc.strokeStyle=stroke;cc.stroke();}}
path([[0,0],[c,1],[R,1]],'rgba(255,182,93,.18)');path([[0,0],[c,1]],null,'#56d9d0');path([[0,0],[R,1]],null,'#8ea6c8');
path([[0,1.03],[0,0],[top,0]],null,'#465a75');path([[0,t],[R*t,t]],null,'#ffb65d');
for(let i=1;i<=5;i++){let speed=c+(R-c)*i/6,p=pt(speed*t,t);cc.fillStyle='#ffb65d';cc.beginPath();cc.arc(...p,2.7,0,2*Math.PI);cc.fill();}
cc.fillStyle='#94a9c3';cc.font='12px system-ui';cc.fillText('t',12,17);cc.fillText('r ≥ 0',cw-42,ch-10);cc.fillText('1',15,pt(0,1)[1]+4);cc.fillText('0',18,Y+16);
$('gap').textContent=((R-c)*t).toFixed(3)+' u';}
$('model').onchange=()=>{kind=$('model').value;draw();};$('direction').onchange=draw;$('dots').onchange=draw;$('layers').onchange=draw;
$('surfaces').onchange=draw;$('opacity').oninput=draw;
$('play').onclick=()=>{running=!running;$('play').textContent=running?'Pausar':'Reproducir';};
$('time').oninput=()=>{t=+$('time').value;running=false;$('play').textContent='Reproducir';draw();};
$('reset').onclick=()=>{yaw=.72;pitch=.38;zoom=1;draw();};
$('save').onclick=()=>{let a=document.createElement('a');a.download=`corona-${kind}-t${t.toFixed(2)}.png`;a.href=canvas.toDataURL();a.click();};
canvas.onpointerdown=e=>{drag=[e.clientX,e.clientY];canvas.setPointerCapture(e.pointerId);};canvas.onpointerup=()=>drag=null;canvas.onpointercancel=()=>drag=null;
canvas.onpointermove=e=>{if(!drag)return;yaw+=(e.clientX-drag[0])*.008;pitch=Math.max(-1.4,Math.min(1.4,pitch+(e.clientY-drag[1])*.008));drag=[e.clientX,e.clientY];draw();};
canvas.onwheel=e=>{e.preventDefault();zoom=Math.max(.5,Math.min(2,zoom*Math.exp(-e.deltaY*.001)));draw();};
function tick(now){if(running&&last){t+=(now-last)/18000;if(t>1)t=0;draw();}last=now;requestAnimationFrame(tick);}
window.addEventListener('resize',resize);resize();requestAnimationFrame(tick);
</script></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'reports/figures/causal_corona/causal_corona.html')
    args = parser.parse_args()
    raw = list(itertools.product((-1, 1), repeat=3))
    tetra = [[a/math.sqrt(3) for a in v] for v in raw if math.prod(v) == -1]
    # Independent geometric checks on the fixed inputs, not new physics evidence.
    assert all(math.isclose(sum(a*a for a in v), 1) for v in tetra)
    assert all(math.isclose(sum(a*b for a, b in zip(v, w)), -1/3)
               for v, w in itertools.combinations(tetra, 2))
    assert math.isclose(1/max(-3*sum(a*b for a,b in zip(v,tetra[0])) for v in tetra),1)
    face = [-a for a in tetra[0]]
    assert math.isclose(1/max(-3*sum(a*b for a,b in zip(v,face)) for v in tetra),1/3)
    models = {
        'tetra': dict(name='s=4 cíclico · sección tetraédrica', c=1/3, vertices=tetra,
                      edges=list(itertools.combinations(range(4), 2)),
                      faces=list(itertools.combinations(range(4), 3)),
                      sources=['reports/2026-11-06--s4-cyclic-realization.md §6',
                               'scripts/plot_s4_cyclic_realization.py'],
                      explain='Vértices a distancia 1; caras a distancia 1/3. La esfera toca las caras. La corona se abre hacia los vértices. Las capas interiores son tiempos anteriores del mismo tetraedro.'),
        'cube': dict(name='CJWW · sección cúbica', c=1, vertices=raw,
                     edges=[(i,j) for i,j in itertools.combinations(range(8),2)
                            if sum(a!=b for a,b in zip(raw[i],raw[j]))==1],
                     sources=['papers/ir-corona/ir-corona.tex §2, §4'],
                     explain='El cubo tiene caras a distancia 1 y vértices a √3. La bola de radio t toca las caras. La corona queda hacia aristas y vértices. Es la geometría del manuscrito de corona IR.')}
    cube_faces = []
    for axis in range(3):
        transverse = [i for i in range(3) if i != axis]
        for sign in (-1, 1):
            ids = [i for i, v in enumerate(raw) if v[axis] == sign]
            ids.sort(key=lambda i: math.atan2(raw[i][transverse[1]], raw[i][transverse[0]]))
            cube_faces.append(ids)
    models['cube']['faces'] = cube_faces
    out = args.output.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HTML.replace('__DATA__', json.dumps(dict(models=models), ensure_ascii=False)), encoding='utf-8')
    provenance = dict(script='scripts/visualize_causal_corona.py',
                      script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                      working_tree=True, html_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
                      meaning='Geometric illustration. Points are not photons, wave amplitudes or probabilities.',
                      models=models, checks='Unit vertex lengths, mutual dot products, vertex and face radial limits.')
    out.with_suffix('.provenance.json').write_text(json.dumps(provenance,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
