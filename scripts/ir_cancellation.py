"""Exploratory cancellation diagnostic, derived 2026-09-21.
DERIVED FROM ir_precision_N24.py (frozen N=24 contract, unchanged),
sha256 bb607b1b7a1f95a6a8f64c77734c587306d6ef97d7dfe6c28b6842113fba2665.
The frozen contract and its recorded N=24 output live ONLY in that file;
nothing here supersedes them. No recorded output is included here.
Changes relative to the frozen code (all others verbatim):
  1. N read from argv (default 24): N=24 re-checks the frozen numbers,
     N=40 is a new run under the same N^-1/2 cutoff family.
  2. signal() also returns A = 2*sum_y F_y|r_y^dag d_y| + sum_y F_y||d_y||^2;
     rows add A_L and kappa_sum_L = A_L/|L|.
kappa_sum measures cancellation in the final summation only; it does not
bound errors already present in d (FFT, quadrature). Not a certificate.
Run: OPENBLAS_NUM_THREADS=1 python -B ir_cancellation.py 24

2026-09-22 optional direct check, authorized before execution:
--direct --scripts-dir PATH imports exact_blocks from the reviewed repository.
Requires exact Laurent identity with the manually written W; stops on mismatch.
Applies N local steps in a nonperiodic box containing the full reachable support.
Reports absolute/relative field and signal discrepancies; threshold 1e-3 is
an empirical comparison only. Shared symbol, source and r remain limitations.
Default computation unchanged. This revision adds no recorded output.
"""

def diagnostics():
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    alpha = 1 - 1 / (2 * np.sqrt(3))
    C2 = alpha * (alpha + np.sqrt(4 - 3 * alpha**2)) / (2 * (1 - alpha**2))
    C = np.sqrt(C2); Sh = np.sqrt(C2 - 1); ts = np.log(C + Sh)
    Dst = np.sqrt(C**6 - 1); phi = np.log(C**3 + Dst)
    qt = C / Dst; qn = qt * (C2 - 1) * (C2 + 2) / (C2**2 + C2 + 1)
    P = 0.5 * np.array([[1 - alpha, -(1 + 1j * C) * alpha / C2], [-(1 - 1j * C) * alpha / C2, 1 + alpha]])
    s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
    I2 = np.eye(2)
    MB = {"I": I2, "P1": (I2 + s1) / 2, "P2": (I2 + s2) / 2, "P3": (I2 + s3) / 2}
    g = lambda q: (1 - q**2)**2
    kq, wk = leggauss(80); kq = 0.5 * (kq + 1); wk = 0.5 * wk
    rho = np.sqrt(3) - 0.25
    A = 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.cos(kq) * np.sinc(kq * rho / np.pi))
    B = 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.sin(kq) * (np.sin(kq * rho) / (kq * rho)**2 - np.cos(kq * rho) / (kq * rho)))
    cr = np.sqrt(3465) / (64 * np.pi**2)
    Bhat = cr * 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.sinc(kq / 4 / np.pi))
    nvec = np.array([[1, 1 + 1j], [1 - 1j, -1]]) / np.sqrt(3)
    R0 = cr * (A * np.array([0, 1]) - B * (nvec @ np.array([0, 1])))
    Kpref = 128 / (3 * np.pi**2) * np.sqrt(2 * np.pi / qn) * Bhat
    cg = 2 * np.pi / (3 * np.sqrt(3))
    tgrid = np.linspace(0, 12, 6001)
    uh = np.ones(3) / np.sqrt(3)

    def gammas(theta, nf=60):
        nn = np.arange(-nf, nf + 1)
        sp_ = ts + 2j * np.pi * nn; sm_ = ts + 1j * np.pi * (2 * nn + 1)
        Sp = (cg * np.exp(-tgrid[:, None]**2 / (4 * np.sqrt(3) * sp_)) / sp_**4 * np.exp(2j * np.pi * nn * theta)).sum(1).real
        Sm = (cg * np.exp(-tgrid[:, None]**2 / (4 * np.sqrt(3) * sm_)) / sm_**4 * np.exp(1j * np.pi * (2 * nn + 1) * theta)).sum(1).real
        wq = 2 * np.pi * tgrid * np.exp(-qt * tgrid**2)
        return np.trapz(wq * Sp**2, tgrid), np.trapz(wq * Sm**2, tgrid)

    def bN(N, r2):
        return np.sqrt(3465) * np.pi / 8 * N**-1.5 / (2 * np.pi)**3 * 4 * np.pi * (wk * kq**2 * g(kq)) @ np.sinc(np.outer(kq, np.sqrt(r2) / N) / np.pi)

    def tilted_SN(N, L):
        m = np.fft.fftfreq(L) * L
        eta = -2 * np.pi * m / L - 1j * ts
        c = np.cos(eta); s = np.sin(eta); e = np.exp(1j * eta)
        c1, c2, sn1, sn2, e3 = c[:, None, None], c[None, :, None], s[:, None, None], s[None, :, None], e[None, None, :]
        f = (c1 * c2) * c[None, None, :]
        sc = np.exp(-phi)
        Um2 = np.zeros((L, L, L), complex); Um1 = np.full((L, L, L), sc, complex)
        for _ in range(N - 1):
            tmp = 2 * sc * f * Um1; tmp -= sc * sc * Um2
            Um2, Um1 = Um1, tmp
        W11 = (c1 * c2) * e3; W22 = (c1 * c2) / e3; W12 = -c1 * sn2 + 1j * sn1; W21 = c1 * sn2 + 1j * sn1
        return Um1 * W22 - sc * Um2, -Um1 * W12, -Um1 * W21, Um1 * W11 - sc * Um2

    def r_tail(N, Y, nr=24, nth=28, nph=56):
        x, wx = leggauss(nr); kr = 0.5 * (x + 1); wkr = 0.5 * wx
        ct, wct = leggauss(nth); ph = 2 * np.pi * np.arange(nph) / nph
        KQ, CT, PH = np.meshgrid(kr, ct, ph, indexing="ij")
        WQ = ((wkr[:, None, None] * wct[None, :, None]) * (2 * np.pi / nph) * KQ**2 * g(KQ)).reshape(-1)
        st = np.sqrt(1 - CT**2)
        Q = np.stack([KQ * st * np.cos(PH), KQ * st * np.sin(PH), KQ * CT], -1).reshape(-1, 3)
        pq = Q / N; c = np.cos(pq); sn = np.sin(pq); e3 = np.exp(1j * pq[:, 2])
        f = c[:, 0] * c[:, 1] * c[:, 2]
        Um2 = np.zeros_like(f); Um1 = np.ones_like(f)
        for _ in range(N - 1):
            Um2, Um1 = Um1, 2 * f * Um1 - Um2
        W11 = c[:, 0] * c[:, 1] * e3; W12 = -c[:, 0] * sn[:, 1] + 1j * sn[:, 0]
        Md = np.stack([-Um1 * W12, Um1 * W11 - Um2], 0) * WQ
        out = np.zeros((Y.shape[0], 2), complex)
        for i0 in range(0, Y.shape[0], 512):
            out[i0:i0 + 512] = np.exp(-1j * (Y[i0:i0 + 512] @ Q.T) / N) @ Md.T
        return out * np.sqrt(3465) * np.pi / 8 * N**-1.5 / (2 * np.pi)**3


    # New diagnostic, fixed N; all spatial sites retained.
    import json, platform, sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('N',nargs='?',type=int,default=24)
    parser.add_argument('--direct',action='store_true')
    parser.add_argument('--scripts-dir')
    args=parser.parse_args()
    N=args.N
    if N<2: parser.error('N must be at least 2')
    if args.direct and not args.scripts_dir:
        parser.error('--direct requires --scripts-dir')
    R=N/4
    rg=np.arange(-int(R),int(R)+1)
    X=np.array(np.meshgrid(rg,rg,rg,indexing="ij")).reshape(3,-1).T
    r2=np.sum(X**2,axis=1)
    X=X[16*r2<N*N]; r2=np.sum(X**2,axis=1)
    Y=X+N
    F=(1-16*r2/N**2)**2
    b=bN(N,r2)
    source=np.stack([np.sin(np.pi*F/2)*b,
                     -2*np.sin(np.pi*F/4)**2*b],axis=1)
    # sigma2: (U-I)phi = s*b*up + c*b*down.
    def full_field(tilt):
        nonlocal ts, phi
        oldts,oldphi=ts,phi
        if not tilt: ts=0.; phi=0.
        Lgrid=2*(N+int(R))+3
        sn=tilted_SN(N,Lgrid)
        ix=tuple((X%Lgrid).T); iy=tuple((Y%Lgrid).T)
        src=np.zeros((Lgrid,Lgrid,Lgrid,2),complex)
        weight=np.exp(ts*X.sum(1)-ts*np.sqrt(3)*R)
        src[ix]=weight[:,None]*source
        ft=np.fft.fftn(src,axes=(0,1,2))
        d=np.stack([np.fft.ifftn(sn[0]*ft[...,0]+sn[1]*ft[...,1])[iy],
                    np.fft.ifftn(sn[2]*ft[...,0]+sn[3]*ft[...,1])[iy]],axis=1)
        d*=np.exp(N*phi-ts*Y.sum(1)+ts*np.sqrt(3)*R)[:,None]
        ts,phi=oldts,oldphi
        return d
    direct_blocks=None
    direct_metadata={}
    if args.direct:
        import hashlib
        from pathlib import Path
        import sympy as sp
        scripts=Path(args.scripts_dir).resolve()
        sys.path.insert(0,str(scripts))
        import verify_signaling_witness as witness
        import verify_directional_saturation as directional
        for module in (witness,directional):
            path=Path(module.__file__).resolve()
            if path.parent!=scripts:
                raise RuntimeError('Imported module outside requested scripts directory')
            direct_metadata[path.name+'_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        blocks=witness.exact_blocks()
        p=directional.PS
        c=[sp.cos(v) for v in p]; s=[sp.sin(v) for v in p]
        e=sp.exp(sp.I*p[2])
        manual=sp.Matrix([[c[0]*c[1]*e,-c[0]*s[1]+sp.I*s[0]],
                          [c[0]*s[1]+sp.I*s[0],c[0]*c[1]/e]])
        reconstructed=sp.zeros(2)
        for h,mat in blocks.items():
            reconstructed+=mat*sp.exp(sp.I*sum(p[j]*h[j] for j in range(3)))
        if any(directional.laurent(v)!=0 for v in reconstructed-manual):
            raise RuntimeError('Exact symbol comparison failed')
        direct_blocks={tuple(-int(v) for v in h):np.array(mat.H.tolist(),dtype=np.complex128)
                       for h,mat in blocks.items()}
        direct_metadata.update(symbol_exact_match=True,block_count=len(blocks))
        print(json.dumps(dict(event='direct_preflight',**direct_metadata)),flush=True)
    d=full_field(True)
    dreal=full_field(False)
    ddir=None
    if direct_blocks is not None:
        # No modulo indexing, no periodic wrap, no amplitude pruning.
        reach=np.max(np.abs(np.array(list(direct_blocks))),axis=0)
        lo=X.min(axis=0)-N*reach; hi=X.max(axis=0)+N*reach
        shape=tuple(hi-lo+1)
        field=np.zeros(shape+(2,),complex)
        field[tuple((X-lo).T)]=source
        for step in range(N):
            nxt=np.zeros_like(field)
            for h,mat in direct_blocks.items():
                src=tuple(slice(max(0,-v),min(n,n-v)) for n,v in zip(shape,h))
                dst=tuple(slice(max(0,v),min(n,n+v)) for n,v in zip(shape,h))
                for i,j in zip(*np.nonzero(mat)):
                    nxt[dst+(i,)]+=mat[i,j]*field[src+(j,)]
            field=nxt
        ddir=np.zeros_like(d)
        inside=np.all((Y>=lo)&(Y<=hi),axis=1)
        ddir[inside]=field[tuple((Y[inside]-lo).T)]
        direct_metadata.update(box_shape=list(map(int,shape)),
                               field_abs_error=float(np.max(abs(ddir-d))),
                               field_rel_error=float(np.max(abs(ddir-d))/np.max(abs(d))))
        del field,nxt
    def signal(r,d):
        linear=2*np.real(np.sum(F[:,None]*r.conj()*d))
        quadratic=np.sum(F[:,None]*abs(d)**2).real
        A=2*np.sum(F*abs(np.sum(r.conj()*d,axis=1)))+quadratic
        return float(linear+quadratic),float(linear),float(quadratic),float(A)
    def projected(nr,nth,nph):
        # Exact finite Fourier sum of source; real-momentum ball quadrature.
        kr,wr=leggauss(nr); kr=(kr+1)/2/np.sqrt(N); wr=wr/2/np.sqrt(N)
        ct,wct=leggauss(nth); ph=2*np.pi*np.arange(nph)/nph
        KQ,CT,PH=np.meshgrid(kr,ct,ph,indexing="ij")
        st=np.sqrt(1-CT**2)
        Q=np.stack([KQ*st*np.cos(PH),KQ*st*np.sin(PH),KQ*CT],-1).reshape(-1,3)
        WQ=np.broadcast_to(wr[:,None,None]*wct[None,:,None]*(2*np.pi/nph)*KQ**2,KQ.shape).reshape(-1)/(2*np.pi)**3
        out=np.zeros((len(Y),2),complex)
        for start in range(0,len(Q),512):
            p=Q[start:start+512]; weights=WQ[start:start+512]
            hat=np.exp(1j*(p@X.T))@source
            c=np.cos(p); s=np.sin(p); e=np.exp(1j*p[:,2])
            f=c[:,0]*c[:,1]*c[:,2]
            um2=np.zeros_like(f); um1=np.ones_like(f)
            for _ in range(N-1): um2,um1=um1,2*f*um1-um2
            s11=c[:,0]*c[:,1]/e
            s22=c[:,0]*c[:,1]*e
            s12=c[:,0]*s[:,1]-1j*s[:,0]
            s21=-c[:,0]*s[:,1]-1j*s[:,0]
            evolved=np.stack([(um1*s11-um2)*hat[:,0]+um1*s12*hat[:,1],
                              um1*s21*hat[:,0]+(um1*s22-um2)*hat[:,1]],axis=1)
            out+=np.exp(-1j*(Y@p.T))@(weights[:,None]*evolved)
        return out
    rows=[]
    prev=None
    for nr,nth,nph in [(12,16,32),(18,24,48),(24,32,64)]:
        r=r_tail(N,Y,nr=nr,nth=nth,nph=nph)
        dp=projected(nr,nth,nph)
        L,lin,quad,A_L=signal(r,d)
        Lpp,linpp,quadpp,_=signal(r,dp)
        Lreal=signal(r,dreal)[0]
        row=dict(N=N,orders=[nr,nth,nph],L=L,L_linear=lin,L_quadratic=quad,
                 Lpp=Lpp,Lpp_linear=linpp,Lpp_quadratic=quadpp,
                 residual=L-Lpp,residual_over_L=(L-Lpp)/L,
                 full_fft_difference=abs(L-Lreal),
                 A_L=A_L,kappa_sum_L=A_L/abs(L))
        if prev is not None:
            row["delta_Lpp"]=abs(Lpp-prev["Lpp"])
            row["delta_L"]=abs(L-prev["L"])
            row["delta_Lpp_over_abs_L"]=abs(Lpp-prev["Lpp"])/abs(L)
        if ddir is not None:
            Ldir=signal(r,ddir)[0]
            row.update(L_direct=Ldir,L_direct_abs_error=abs(Ldir-L),
                       L_direct_rel_error=abs(Ldir-L)/abs(L),**direct_metadata)
            row['direct_empirical_pass']=(row['L_direct_rel_error']<1e-3
                                          and row['field_rel_error']<1e-3)
        print(json.dumps(row),flush=True)
        rows.append(row); prev=row
    print(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,
                          sites=len(X),field_fft_max_difference=float(np.max(abs(d-dreal))),
                          criterion=1e-3,
                          empirical_precision_pass=rows[-1]["delta_Lpp_over_abs_L"]<1e-3
                          and rows[-1]["full_fft_difference"]<1e-3*abs(rows[-1]["L"]))),flush=True)

if __name__=="__main__":
    diagnostics()
