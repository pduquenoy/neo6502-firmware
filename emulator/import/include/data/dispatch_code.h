//
//	This file is automatically generated
//
switch (*DCOMMAND) {
	case 1:
		switch (*DFUNCTION) {
			case 0:
				DSPReset();
				break;
			case 1:
				*((uint32_t *)DPARAMS) = TMRRead();
				break;
			case 2:
				i1 = *DPARAMS;
				*DPARAMS = (i1 < KBD_MAX_KEYCODE) ? KBDGetStateArray()[i1] : 0;
				break;
			case 3:
				MEMLoadBasic();
				break;
			case 4:
				CONWriteString((char *)whoList);
				break;
		}
		break;
	case 2:
		switch (*DFUNCTION) {
			case 0:
				CONWrite(*DPARAMS);
				break;
			case 1:
				*(DPARAMS) = KBDGetKey();
				break;
			case 2:
				*(DPARAMS) = KBDIsKeyAvailable() ? 0xFF: 0;
				break;
			case 3:
				CONGetScreenLine(DSPGetInt16(DCOMMAND,4));
				break;
			case 4:
				*DERROR = KBDSetFunctionKey(*(DCOMMAND+4),DSPGetString(DCOMMAND,6));
				break;
		}
		break;
	case 3:
		switch (*DFUNCTION) {
			case 1:
				FIODirectory();
				break;
			case 2:
				*DERROR = FIOReadFile(DSPGetString(DCOMMAND,4),DSPGetInt16(DCOMMAND,6));
				break;
			case 3:
				*DERROR = FIOWriteFile(DSPGetString(DCOMMAND,4),DSPGetInt16(DCOMMAND,6),DSPGetInt16(DCOMMAND,8));
				break;
		}
		break;
	case 4:
		MATHCommon(DPARAMS);
		switch (*DFUNCTION) {
			case 0:
				if (MATHIsFloatBinary()) {
				MATHWriteFloat(MATHReadFloat(MATH_REG1)+MATHReadFloat(MATH_REG2),MATH_REG1);
				} else {
				MATHWriteInt(MATHReadInt(MATH_REG1)+MATHReadInt(MATH_REG2),MATH_REG1);
				}
				break;
			case 1:
				if (MATHIsFloatBinary()) {
				MATHWriteFloat(MATHReadFloat(MATH_REG1)-MATHReadFloat(MATH_REG2),MATH_REG1);
				} else {
				MATHWriteInt(MATHReadInt(MATH_REG1)-MATHReadInt(MATH_REG2),MATH_REG1);
				}
				break;
			case 2:
				if (MATHIsFloatBinary()) {
				MATHWriteFloat(MATHReadFloat(MATH_REG1)*MATHReadFloat(MATH_REG2),MATH_REG1);
				} else {
				MATHWriteInt(MATHReadInt(MATH_REG1)*MATHReadInt(MATH_REG2),MATH_REG1);
				}
				break;
			case 3:
				f2 = MATHReadFloat(MATH_REG2);
				if (f2 == 0.0) {
				*DERROR = 1;
				} else {
				MATHWriteFloat(MATHReadFloat(MATH_REG1)/f2,MATH_REG1);
				}
				break;
			case 4:
				i1 = MATHReadInt(MATH_REG1);
				i2 = MATHReadInt(MATH_REG2);
				if (i2 == 0) {
				*DERROR = 1;
				} else {
				MATHWriteInt(i1/i2,MATH_REG1);
				}
				break;
			case 5:
				i1 = MATHReadInt(MATH_REG1);
				i2 = MATHReadInt(MATH_REG2);
				if (i2 == 0) {
				*DERROR = 1;
				} else {
				MATHWriteInt(abs(i1) % abs(i2),MATH_REG1);
				}
				break;
			case 6:
				r = 0;
				if (MATHIsFloatBinary()) {
				f1 = MATHReadFloat(MATH_REG1);
				f2 = MATHReadFloat(MATH_REG2);
				float diff = (float_abs(f1)+float_abs(f2)) * 0.0000001f;
				if (float_abs(f1-f2) >= diff) {
				r = (f1 < f2 ? 0xFF:0x01);
				}
				} else {
				i1 = MATHReadInt(MATH_REG1);
				i2 = MATHReadInt(MATH_REG2);
				if (i1 != i2) r = (i1 < i2 ? 0xFF:0x01);
				}
				*DPARAMS = r;
				#define FROMRADIANS(n) 	((n) * 180.0 / M_PI)
				#define TORADIANS(n) ((n) * M_PI / 180.0)
				break;
			case 16:
				if (MATHIsFloatUnary()) {
				MATHWriteFloat(-MATHReadFloat(MATH_REG1),MATH_REG1);
				} else {
				MATHWriteInt(-MATHReadInt(MATH_REG1),MATH_REG1);
				}
				break;
			case 17:
				if (MATHIsFloatBinary()) {
				MATHWriteInt(MATHReadInt(MATH_REG1),MATH_REG1);
				}
				break;
			case 18:
				f1 = MATHReadFloat(MATH_REG1);
				if (f1 >= 0) {
				MATHWriteFloat(sqrt(f1),MATH_REG1);
				} else {
				*DERROR = 1;
				}
				break;
			case 19:
				f1 = MATHReadFloat(MATH_REG1);
				MATHWriteFloat(sin(TORADIANS(f1)),MATH_REG1);
				break;
			case 20:
				f1 = MATHReadFloat(MATH_REG1);
				MATHWriteFloat(cos(TORADIANS(f1)),MATH_REG1);
				break;
			case 21:
				f1 = MATHReadFloat(MATH_REG1);
				MATHWriteFloat(tan(TORADIANS(f1)),MATH_REG1);
				break;
			case 22:
				f1 = MATHReadFloat(MATH_REG1);
				MATHWriteFloat(FROMRADIANS(atan(f1)),MATH_REG1);
				break;
			case 23:
				f1 = MATHReadFloat(MATH_REG1);
				MATHWriteFloat(exp(f1),MATH_REG1);
				break;
			case 24:
				f1 = MATHReadFloat(MATH_REG1);
				if (f1 >= 0) {
				MATHWriteFloat(log(f1),MATH_REG1);
				} else {
				*DERROR = 1;
				}
				break;
			case 25:
				if (MATHIsFloatUnary()) {
				MATHWriteFloat(fabs(MATHReadFloat(MATH_REG1)),MATH_REG1);
				} else {
				u1 = MATHReadInt(MATH_REG1);
				if (u1 & 0x80000000) {
				MATHWriteInt(-u1,MATH_REG1);
				}
				}
				break;
			case 26:
				u1 = 0;
				if (MATHIsFloatUnary()) {
				f1 = MATHReadFloat(MATH_REG1);
				if (f1 != 0.0) u1 = (f1 < 0) ? -1 : 1;
				} else {
				i1 = MATHReadInt(MATH_REG1);
				if (i1 != 0) u1 = (i1 < 0) ? -1 : 1;
				}
				MATHWriteInt(u1,MATH_REG1);
				break;
			case 27:
				f1 = (rand() % 100000) / 100000.0;
				MATHWriteFloat(f1,MATH_REG1);
				break;
			case 28:
				u1 = MATHReadInt(MATH_REG1);
				if (u1 > 0) {
				MATHWriteInt(rand() % u1,MATH_REG1);
				}
				break;
			case 32:
				MATHProcessDecimal(DCOMMAND);
				break;
			case 33:
				MATHConvertStringToNumber(DCOMMAND);
				break;
			case 34:
				MATHConvertNumberToString(DCOMMAND);
				break;
		}
		break;
	case 5:
		switch (*DFUNCTION) {
			case 1:
				GFXSetDefaults(DCOMMAND);
				break;
			case 2:
				GFXGraphicsCommand(2,DCOMMAND);
				break;
			case 3:
				GFXGraphicsCommand(3,DCOMMAND);
				break;
			case 4:
				GFXGraphicsCommand(4,DCOMMAND);
				break;
			case 5:
				GFXGraphicsCommand(5,DCOMMAND);
				break;
			case 6:
				GFXGraphicsCommand(6,DCOMMAND);
				break;
			case 7:
				GFXGraphicsCommand(7,DCOMMAND);
				break;
			case 32:
				gMode.setPalette(DPARAMS[0],DPARAMS[1],DPARAMS[2],DPARAMS[3]);
				break;
		}
		break;
	case 7:
		switch (*DFUNCTION) {
			case 1:
				*DPARAMS = KBDKeyboardController();
				break;
		}
		break;
}
