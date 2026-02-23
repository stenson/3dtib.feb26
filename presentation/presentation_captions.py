from coldtype import *

font = "NYC_Sans_v0.3_Variable.ttf"

captions = [
    "Claes Oldenburg & Coosje van Bruggen",
    "Takenobu Igarashi",
    "Carlo Scarpa",
    "Walter Gropius (?)",
    "Renzo Piano",
    "Erik van Blokland",
    "Tod Williams Billie Tsien Architects",
    "Thom Mayne",
    "László Moholy-Nagy",
    "Norman Ives",
    "Dan Perri",
    "Corita Kent",
    "Max Huber",
    "Inada Sousai",
    "Reid Miles",
    "TBWA\\Media Arts Lab",
    "GMUNK",
]

@animation((2000, 80)
    , bg=-1
    , suffixer=lambda i: re.sub(r"\(\)\s\_\?", "", captions[i].lower())
    , tl=Timeline(len(captions)))
def cap(f:Frame):
    return (StSt(captions[f.i], font, 30, wght=0.5)
        .align(f.a.r)
        .f(1)
        .pen()
        .intersection(l:=lambda p: P().rect(p.ambit(tx=0, ty=0).inset(-20, -6)).f(0))
        .up()
        .insert(0, l))
