#
#		Convert font to 6x8 ordered.
#
lcdfont = [
	 0x00, 0x00, 0x00, 0x00, 0x00 ,  # 20  32
	 0x00, 0x00, 0x4F, 0x00, 0x00 ,  # 21  33  !
	 0x00, 0x07, 0x00, 0x07, 0x00 ,  # 22  34  "
	 0x14, 0x7F, 0x14, 0x7F, 0x14 ,  # 23  35  #
	 0x24, 0x2A, 0x7F, 0x2A, 0x12 ,  # 24  36  $
	 0x23, 0x13, 0x08, 0x64, 0x62 ,  # 25  37  %
	 0x36, 0x49, 0x55, 0x22, 0x50 ,  # 26  38  &
	 0x00, 0x05, 0x03, 0x00, 0x00 ,  # 27  39  '
	 0x00, 0x1C, 0x22, 0x41, 0x00 ,  # 28  40  (
	 0x00, 0x41, 0x22, 0x1C, 0x00 ,  # 29  41  )
	 0x14, 0x08, 0x3E, 0x08, 0x14 ,  # 2A  42  *
	 0x08, 0x08, 0x3E, 0x08, 0x08 ,  # 2B  43  +
	 0x00, 0x50, 0x30, 0x00, 0x00 ,  # 2C  44  ,
	 0x08, 0x08, 0x08, 0x08, 0x08 ,  # 2D  45  -
	 0x00, 0x60, 0x60, 0x00, 0x00 ,  # 2E  46  .
	 0x20, 0x10, 0x08, 0x04, 0x02 ,  # 2F  47  /
	 0x3E, 0x51, 0x49, 0x45, 0x3E ,  # 30  48  0
	 0x00, 0x42, 0x7F, 0x40, 0x00 ,  # 31  49  1
	 0x42, 0x61, 0x51, 0x49, 0x46 ,  # 32  50  2
	 0x21, 0x41, 0x45, 0x4B, 0x31 ,  # 33  51  3
	 0x18, 0x14, 0x12, 0x7F, 0x10 ,  # 34  52  4
	 0x27, 0x45, 0x45, 0x45, 0x39 ,  # 35  53  5
	 0x3C, 0x4A, 0x49, 0x49, 0x30 ,  # 36  54  6
	 0x03, 0x01, 0x71, 0x09, 0x07 ,  # 37  55  7
	 0x36, 0x49, 0x49, 0x49, 0x36 ,  # 38  56  8
	 0x06, 0x49, 0x49, 0x29, 0x1E ,  # 39  57  9
	 0x00, 0x36, 0x36, 0x00, 0x00 ,  # 3A  58  :
	 0x00, 0x56, 0x36, 0x00, 0x00 ,  # 3B  59  ;
	 0x08, 0x14, 0x22, 0x41, 0x00 ,  # 3C  60  <
	 0x14, 0x14, 0x14, 0x14, 0x14 ,  # 3D  61  =
	 0x00, 0x41, 0x22, 0x14, 0x08 ,  # 3E  62  >
	 0x02, 0x01, 0x51, 0x09, 0x06 ,  # 3F  63  ?
	 0x32, 0x49, 0x79, 0x41, 0x3E ,  # 40  64  @
	 0x7E, 0x11, 0x11, 0x11, 0x7E ,  # 41  65  A
	 0x7F, 0x49, 0x49, 0x49, 0x36 ,  # 42  66  B
	 0x3E, 0x41, 0x41, 0x41, 0x22 ,  # 43  67  C
	 0x7F, 0x41, 0x41, 0x22, 0x1C ,  # 44  68  D
	 0x7F, 0x49, 0x49, 0x49, 0x41 ,  # 45  69  E
	 0x7F, 0x09, 0x09, 0x09, 0x01 ,  # 46  70  F
	 0x3E, 0x41, 0x49, 0x49, 0x7A ,  # 47  71  G
	 0x7F, 0x08, 0x08, 0x08, 0x7F ,  # 48  72  H
	 0x00, 0x41, 0x7F, 0x41, 0x00 ,  # 49  73  I
	 0x20, 0x40, 0x41, 0x3F, 0x01 ,  # 4A  74  J
	 0x7F, 0x08, 0x14, 0x22, 0x41 ,  # 4B  75  K
	 0x7F, 0x40, 0x40, 0x40, 0x40 ,  # 4C  76  L
	 0x7F, 0x02, 0x0C, 0x02, 0x7F ,  # 4D  77  M
	 0x7F, 0x04, 0x08, 0x10, 0x7F ,  # 4E  78  N
	 0x3E, 0x41, 0x41, 0x41, 0x3E ,  # 4F  79  O
	 0x7F, 0x09, 0x09, 0x09, 0x06 ,  # 50  80  P
	 0x3E, 0x41, 0x51, 0x21, 0x5E ,  # 51  81  Q
	 0x7F, 0x09, 0x19, 0x29, 0x46 ,  # 52  82  R
	 0x46, 0x49, 0x49, 0x49, 0x31 ,  # 53  83  S
	 0x01, 0x01, 0x7F, 0x01, 0x01 ,  # 54  84  T
	 0x3F, 0x40, 0x40, 0x40, 0x3F ,  # 55  85  U
	 0x1F, 0x20, 0x40, 0x20, 0x1F ,  # 56  86  V
	 0x3F, 0x40, 0x38, 0x40, 0x3F ,  # 57  87  W
	 0x63, 0x14, 0x08, 0x14, 0x63 ,  # 58  88  X
	 0x07, 0x08, 0x70, 0x08, 0x07 ,  # 59  89  Y
	 0x61, 0x51, 0x49, 0x45, 0x43 ,  # 5A  90  Z
	 0x7F, 0x41, 0x41, 0x00, 0x00 ,  # 5B  91  h
	 0x15, 0x16, 0x7C, 0x16, 0x15 ,  # 5C  92  '\'
	 0x00, 0x41, 0x41, 0x7F, 0x00 ,  # 5D  93  ]
	 0x04, 0x02, 0x01, 0x02, 0x04 ,  # 5E  94  ^
	 0x40, 0x40, 0x40, 0x40, 0x40 ,  # 5F  95  _
	 0x00, 0x01, 0x02, 0x04, 0x00 ,  # 60  96  `
	 0x20, 0x54, 0x54, 0x54, 0x78 ,  # 61  97  a
	 0x7F, 0x48, 0x44, 0x44, 0x38 ,  # 62  98  b
	 0x38, 0x44, 0x44, 0x44, 0x20 ,  # 63  99  c
	 0x38, 0x44, 0x44, 0x48, 0x7F ,  # 64 100  d
	 0x38, 0x54, 0x54, 0x54, 0x18 ,  # 65 101  e
	 0x08, 0x7E, 0x09, 0x01, 0x02 ,  # 66 102  f
	 0x0C, 0x52, 0x52, 0x52, 0x3E ,  # 67 103  g
	 0x7F, 0x08, 0x04, 0x04, 0x78 ,  # 68 104  h
	 0x00, 0x44, 0x7D, 0x40, 0x00 ,  # 69 105  i
	 0x20, 0x40, 0x44, 0x3D, 0x00 ,  # 6A 106  j
	 0x7F, 0x10, 0x28, 0x44, 0x00 ,  # 6B 107  k
	 0x00, 0x41, 0x7F, 0x40, 0x00 ,  # 6C 108  l
	 0x7C, 0x04, 0x18, 0x04, 0x78 ,  # 6D 109  m
	 0x7C, 0x08, 0x04, 0x04, 0x78 ,  # 6E 110  n
	 0x38, 0x44, 0x44, 0x44, 0x38 ,  # 6F 111  o
	 0x7C, 0x14, 0x14, 0x14, 0x08 ,  # 70 112  p
	 0x08, 0x14, 0x14, 0x18, 0x7C ,  # 71 113  q
	 0x7C, 0x08, 0x04, 0x04, 0x08 ,  # 72 114  r
	 0x48, 0x54, 0x54, 0x54, 0x20 ,  # 73 115  s
	 0x04, 0x3F, 0x44, 0x40, 0x20 ,  # 74 116  t
	 0x3C, 0x40, 0x40, 0x20, 0x7C ,  # 75 117  u
	 0x1C, 0x20, 0x40, 0x20, 0x1C ,  # 76 118  v
	 0x3C, 0x40, 0x38, 0x40, 0x3C ,  # 77 119  w
	 0x44, 0x28, 0x10, 0x28, 0x44 ,  # 78 120  x
	 0x0C, 0x50, 0x50, 0x50, 0x3C ,  # 79 121  y
	 0x44, 0x64, 0x54, 0x4C, 0x44 ,  # 7A 122  z
	 0x00, 0x08, 0x36, 0x41, 0x00 ,  # 7B 123  
	 0x00, 0x00, 0x7F, 0x00, 0x00 ,  # 7C 124  |
	 0x00, 0x41, 0x36, 0x08, 0x00 ,  # 7D 125  
	 0x08, 0x08, 0x2A, 0x1C, 0x08 ,  # 7E 126  ~
	 0x08, 0x1C, 0x2A, 0x08, 0x08    # 7F 127
]

for c in range(0,96):
	font = [ 0 ] * 8
	for col in range(0,5):
		b = lcdfont[c * 5 + col]
		for row in range(0,8):
			if (b & (1 << row)) != 0:
				font[row] += (0x80 >> col)
	print("{0},".format(",".join(["0x{0:02x}".format(x) for x in font])))				