#PI Gherkin by Dora

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
#enables double taps and hold to change characters
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance

#set up for double characters like '=='
from kmk.handlers.sequences import send_string

from kmk.extensions.peg_oled_Display import (
    Oled, OledDisplayMode, OledReactionType, OledData)


keyboard = KMKKeyboard()

tapdance = TapDance()
tapdance.tap_time = 350

modtap = ModTap()
layers_ext = Layers()
keyboard.modules = [layers_ext, modtap, tapdance]

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["0","1","2","3"]},
        corner_three={0:OledReactionType.LAYER,1:["base","raise","toggleq","adjust"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","numbers","punct","Gamer"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)

keyboard.extensions.append(oled_ext)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

CTL_X = KC.MT(KC.X, KC.LCTL)
SPC_LYR2 = KC.MT(KC.SPC, KC.MO(2))

TAB_SHIFT_TD = KC.TD(
    #tap once for tab, hold for shift
    KC.MT(KC.TAB, KC.RSFT),
    #tap twice for enter
    KC.ENT,
)

Q_ESC_TD = KC.TD(
    KC.Q,
    KC.ESC,
)

G_PRN_TD = KC.TD(
    KC.G,
    KC.LPRN,
    KC.RPRN,
)

HASH_TD = KC.TD(
    KC.H,
    KC.HASH,
)

Y_COMM_TD = KC.TD(
    KC.Y,
    KC.COMMA,
    KC.DOT,
)

T_CLN_TD = KC.TD(
    KC.T,
    KC.COLN,
    KC.SCLN,
)

J_QUO_TD = KC.TD(
    KC.J,
    KC.QUOT,
    KC.DQUO,
)

U_UND_TD = KC.TD(
    KC.U,
    KC.UNDS,
)

V_AT_TD = KC.TD(
    KC.U,
    KC.AT,
)

A_NOTEQ_TD = KC.TD(
    KC.A,
    send_string('!='),
)

S_EQ_TD = KC.TD(
    KC.S,
    send_string('==')
)

DLR_PLEQ_TD = KC.TD(
    KC.DLR,
    send_string('+=')
)

LSB_MIEQ_TD = KC.TD(
    KC.LBRC,
    send_string('-=')
)

LCB_LEQ_TD = KC.TD(
    KC.LCBR,
    send_string('<=')
    )

RCB_GREQ_TD = KC.TD(
    KC.RCBR,
    send_string('>=')
)

#XXXXXXX is a faulty key due to poor solder job
#Keyboard is backwards to keep cable on preferred side
keyboard.keymap = [
    [
        SPC_LYR2, TAB_SHIFT_TD, KC.M, KC.N,     KC.B,       V_AT_TD,     KC.C,  CTL_X, KC.Z,    KC.TG(1),
        XXXXXXX,  KC.L,         KC.K, J_QUO_TD, HASH_TD,    G_PRN_TD, KC.F,  KC.D,  S_EQ_TD, A_NOTEQ_TD,
        KC.P,     KC.O,         KC.I, U_UND_TD, Y_COMM_TD,  T_CLN_TD, KC.R,  KC.E,  KC.W,    Q_ESC_TD
    ],

    #Layer 1 Number
    [
        _______, _______,  KC.PIPE,  KC.RABK,  KC.CIRC,  KC.N0,    KC.N3,  KC.N2,  KC.N1,  _______,
        XXXXXXX, _______,  KC.BSLS,  KC.LABK,  KC.PERC,  KC.ASTR,  KC.N6,  KC.N5,  KC.N4,  _______,
        _______, _______,  KC.SLSH,  KC.EQL,   KC.MINS,  KC.PLUS,  KC.N9,  KC.N8,  KC.N7,  KC.TG(3)
    ],

    #Layer 2 Punctuation
    [
        _______,  KC.QUES, KC.COMMA, KC.DOT,  _______, KC.SCLN, KC.COLN,     KC.GRV,      KC.TILD,    _______,
        XXXXXXX,  KC.EXLM, KC.QUOT,  KC.DQUO, _______, KC.RBRC, LSB_MIEQ_TD, RCB_GREQ_TD, LCB_LEQ_TD, KC.BSPC,
        _______, KC.HASH,  KC.AT,    KC.UNDS, _______, KC.AMPR, DLR_PLEQ_TD, KC.RPRN,     KC.LPRN,    _______
    ],

    #Layer 3 game testing
    [
        _______, _______,  _______, _______,   KC.N5,    KC.N4,  KC.N3,  KC.N2,  KC.N1,   _______,
        _______, _______, _______, _______,    _______,   KC.D, KC.S,    KC.A,  _______, _______,
        _______, _______, _______,  _______,  _______,    KC.E, KC.W,    KC.Q,   _______,  _______
    ],

#Left Blank for potiential future use
    [
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,  _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______
    ],
]

if __name__ == '__main__':
    keyboard.go()
