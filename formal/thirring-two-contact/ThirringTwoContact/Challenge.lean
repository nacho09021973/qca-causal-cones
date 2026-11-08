import Std

/-!
Readable exact finite challenge. No theorem or proof is imported from the
scientific project. Coefficients are pairs of integers (real, imaginary).
Each free two-particle step has denominator 25: nu=4/5, mu=3/5.
The eight-site ring has no wrapping on the initial support {2,3} through
two steps. The identification with fermionic Fock space is NOT formalized.
-/
namespace ThirringChallenge

abbrev G := Int × Int
def zero : G := (0,0)
def one : G := (1,0)
def add (a b : G) : G := (a.1+b.1,a.2+b.2)
def neg (a : G) : G := (-a.1,-a.2)
def mul (a b : G) : G := (a.1*b.1-a.2*b.2,a.1*b.2+a.2*b.1)
def conj (a : G) : G := (a.1,-a.2)
def scale (n : Int) (a : G) : G := (n*a.1,n*a.2)
def normSq (a : G) : Int := a.1*a.1+a.2*a.2
def sumG (n : Nat) (f : Nat → G) : G :=
  (List.range n).foldl (fun acc k => add acc (f k)) zero

abbrev Amp := Nat → Nat → G
def perm (plus : Bool) (x : Nat) : Nat :=
  if (x % 2 == 0) == plus then (x+1)%8 else (x+7)%8
def input (j : Nat) : Amp := fun x y =>
  if x == 2+j/2 && y == 3-j%2 then one else zero
def contact (v : Amp) : Amp := fun x y =>
  if x == y then mul (0,1) (v x y) else v x y
def free (plus : Bool) (v : Amp) : Amp := fun x y =>
  add (add (scale 16 (v (perm plus x) (perm (!plus) y)))
           (mul (0,-12) (v (perm plus x) y)))
      (add (mul (0,-12) (v x (perm (!plus) y))) (scale (-9) (v x y)))
def step (plus : Bool) (v : Amp) : Amp := free plus (contact v)
def free1 (j : Nat) : Amp := free true (input j)
def actual1 (j : Nat) : Amp := step true (input j)
def free2 (j : Nat) : Amp := free false (free1 j)
def actual2 (j : Nat) : Amp := step false (actual1 j)
def inner (a b : Amp) : G := sumG 8 fun x =>
  sumG 8 fun y => mul (conj (a x y)) (b x y)

def phase (j : Nat) : G := if j == 1 || j == 2 then (0,1) else one
def kNum (a b : Nat) : G :=
  if a == b then (if a == 0 || a == 3 then (481,144) else (-81,544))
  else if a == 0 && b == 2 || a == 3 && b == 1 then (-108,108)
  else if a == 2 && b == 0 || a == 1 && b == 3 then (-108,-108)
  else zero
def hNum (a b : Nat) : Int :=
  if a == b then (if a == 0 || a == 3 then 16 else 9)
  else if a == 0 && b == 2 || a == 2 && b == 0 ||
          a == 1 && b == 3 || a == 3 && b == 1 then 12 else 0

def FirstGate : Prop := ∀ j : Fin 4, ∀ x y : Fin 8,
  actual1 j x y = mul (free1 j x y) (phase j)
def FreeGram : Prop := ∀ a b : Fin 4,
  inner (free2 a) (free2 b) = if a == b then (390625,0) else zero
def ActualGram : Prop := ∀ a b : Fin 4,
  inner (actual2 a) (actual2 b) = if a == b then (390625,0) else zero
def SecondCompression : Prop := ∀ a b : Fin 4,
  inner (free2 a) (actual2 b) = scale 625 (kNum a b)
def DefectGram : Prop := ∀ a b : Fin 4,
  sumG 4 (fun k => mul (conj (kNum k a)) (kNum k b)) =
    ((if a == b then 390625 else 0)-7200*hNum a b,0)
def ProjectorIdentity : Prop := ∀ a b : Fin 4,
  (List.range 4).foldl (fun acc k => acc + hNum a k * hNum k b) (0 : Int) =
    25*hNum a b
def WitnessEigenvector : Prop := ∀ a : Fin 4,
  hNum a 0*4+hNum a 2*3 = 25*(if a == 0 then 4 else if a == 2 then 3 else 0)
def StrictColumnDefect : Prop :=
  (List.range 4).foldl (fun acc k => acc + normSq (kNum k 0)) (0 : Int) = 275425 ∧
  (390625 : Int)-275425 = 115200 ∧ (0 : Int) < 115200
def NoWrap : Prop := ∀ j : Fin 4, ∀ x y : Fin 8,
  5 < x.val ∨ 5 < y.val → actual2 j x y = zero ∧ free2 j x y = zero

end ThirringChallenge
