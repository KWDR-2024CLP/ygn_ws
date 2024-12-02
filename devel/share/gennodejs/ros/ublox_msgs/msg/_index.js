
"use strict";

let NavDGPS_SV = require('./NavDGPS_SV.js');
let MonHW = require('./MonHW.js');
let NavSTATUS = require('./NavSTATUS.js');
let EsfSTATUS_Sens = require('./EsfSTATUS_Sens.js');
let NavHPPOSECEF = require('./NavHPPOSECEF.js');
let MonVER = require('./MonVER.js');
let EsfSTATUS = require('./EsfSTATUS.js');
let RxmRTCM = require('./RxmRTCM.js');
let CfgMSG = require('./CfgMSG.js');
let CfgDAT = require('./CfgDAT.js');
let NavSAT_SV = require('./NavSAT_SV.js');
let AidEPH = require('./AidEPH.js');
let NavRELPOSNED = require('./NavRELPOSNED.js');
let NavTIMEUTC = require('./NavTIMEUTC.js');
let NavRELPOSNED9 = require('./NavRELPOSNED9.js');
let CfgRATE = require('./CfgRATE.js');
let RxmRAW = require('./RxmRAW.js');
let EsfMEAS = require('./EsfMEAS.js');
let RxmRAW_SV = require('./RxmRAW_SV.js');
let CfgINF = require('./CfgINF.js');
let MgaGAL = require('./MgaGAL.js');
let CfgINF_Block = require('./CfgINF_Block.js');
let RxmEPH = require('./RxmEPH.js');
let RxmSFRB = require('./RxmSFRB.js');
let EsfRAW_Block = require('./EsfRAW_Block.js');
let CfgTMODE3 = require('./CfgTMODE3.js');
let NavPOSECEF = require('./NavPOSECEF.js');
let NavSBAS_SV = require('./NavSBAS_SV.js');
let CfgUSB = require('./CfgUSB.js');
let CfgRST = require('./CfgRST.js');
let CfgHNR = require('./CfgHNR.js');
let NavSVIN = require('./NavSVIN.js');
let RxmSFRBX = require('./RxmSFRBX.js');
let UpdSOS = require('./UpdSOS.js');
let NavTIMEGPS = require('./NavTIMEGPS.js');
let CfgNAVX5 = require('./CfgNAVX5.js');
let CfgANT = require('./CfgANT.js');
let CfgCFG = require('./CfgCFG.js');
let RxmALM = require('./RxmALM.js');
let Inf = require('./Inf.js');
let NavSOL = require('./NavSOL.js');
let NavHPPOSLLH = require('./NavHPPOSLLH.js');
let MonHW6 = require('./MonHW6.js');
let NavVELNED = require('./NavVELNED.js');
let CfgNMEA = require('./CfgNMEA.js');
let EsfINS = require('./EsfINS.js');
let NavCLOCK = require('./NavCLOCK.js');
let NavSBAS = require('./NavSBAS.js');
let CfgSBAS = require('./CfgSBAS.js');
let NavATT = require('./NavATT.js');
let MonGNSS = require('./MonGNSS.js');
let MonVER_Extension = require('./MonVER_Extension.js');
let CfgPRT = require('./CfgPRT.js');
let NavSVINFO = require('./NavSVINFO.js');
let HnrPVT = require('./HnrPVT.js');
let CfgNMEA6 = require('./CfgNMEA6.js');
let NavDGPS = require('./NavDGPS.js');
let NavSAT = require('./NavSAT.js');
let NavSVINFO_SV = require('./NavSVINFO_SV.js');
let NavDOP = require('./NavDOP.js');
let CfgNMEA7 = require('./CfgNMEA7.js');
let NavPVT = require('./NavPVT.js');
let RxmSVSI_SV = require('./RxmSVSI_SV.js');
let CfgGNSS_Block = require('./CfgGNSS_Block.js');
let NavPOSLLH = require('./NavPOSLLH.js');
let EsfRAW = require('./EsfRAW.js');
let NavPVT7 = require('./NavPVT7.js');
let UpdSOS_Ack = require('./UpdSOS_Ack.js');
let EsfALG = require('./EsfALG.js');
let TimTM2 = require('./TimTM2.js');
let CfgGNSS = require('./CfgGNSS.js');
let CfgNAV5 = require('./CfgNAV5.js');
let RxmRAWX_Meas = require('./RxmRAWX_Meas.js');
let RxmSVSI = require('./RxmSVSI.js');
let AidALM = require('./AidALM.js');
let AidHUI = require('./AidHUI.js');
let NavVELECEF = require('./NavVELECEF.js');
let Ack = require('./Ack.js');
let CfgDGNSS = require('./CfgDGNSS.js');
let RxmRAWX = require('./RxmRAWX.js');

module.exports = {
  NavDGPS_SV: NavDGPS_SV,
  MonHW: MonHW,
  NavSTATUS: NavSTATUS,
  EsfSTATUS_Sens: EsfSTATUS_Sens,
  NavHPPOSECEF: NavHPPOSECEF,
  MonVER: MonVER,
  EsfSTATUS: EsfSTATUS,
  RxmRTCM: RxmRTCM,
  CfgMSG: CfgMSG,
  CfgDAT: CfgDAT,
  NavSAT_SV: NavSAT_SV,
  AidEPH: AidEPH,
  NavRELPOSNED: NavRELPOSNED,
  NavTIMEUTC: NavTIMEUTC,
  NavRELPOSNED9: NavRELPOSNED9,
  CfgRATE: CfgRATE,
  RxmRAW: RxmRAW,
  EsfMEAS: EsfMEAS,
  RxmRAW_SV: RxmRAW_SV,
  CfgINF: CfgINF,
  MgaGAL: MgaGAL,
  CfgINF_Block: CfgINF_Block,
  RxmEPH: RxmEPH,
  RxmSFRB: RxmSFRB,
  EsfRAW_Block: EsfRAW_Block,
  CfgTMODE3: CfgTMODE3,
  NavPOSECEF: NavPOSECEF,
  NavSBAS_SV: NavSBAS_SV,
  CfgUSB: CfgUSB,
  CfgRST: CfgRST,
  CfgHNR: CfgHNR,
  NavSVIN: NavSVIN,
  RxmSFRBX: RxmSFRBX,
  UpdSOS: UpdSOS,
  NavTIMEGPS: NavTIMEGPS,
  CfgNAVX5: CfgNAVX5,
  CfgANT: CfgANT,
  CfgCFG: CfgCFG,
  RxmALM: RxmALM,
  Inf: Inf,
  NavSOL: NavSOL,
  NavHPPOSLLH: NavHPPOSLLH,
  MonHW6: MonHW6,
  NavVELNED: NavVELNED,
  CfgNMEA: CfgNMEA,
  EsfINS: EsfINS,
  NavCLOCK: NavCLOCK,
  NavSBAS: NavSBAS,
  CfgSBAS: CfgSBAS,
  NavATT: NavATT,
  MonGNSS: MonGNSS,
  MonVER_Extension: MonVER_Extension,
  CfgPRT: CfgPRT,
  NavSVINFO: NavSVINFO,
  HnrPVT: HnrPVT,
  CfgNMEA6: CfgNMEA6,
  NavDGPS: NavDGPS,
  NavSAT: NavSAT,
  NavSVINFO_SV: NavSVINFO_SV,
  NavDOP: NavDOP,
  CfgNMEA7: CfgNMEA7,
  NavPVT: NavPVT,
  RxmSVSI_SV: RxmSVSI_SV,
  CfgGNSS_Block: CfgGNSS_Block,
  NavPOSLLH: NavPOSLLH,
  EsfRAW: EsfRAW,
  NavPVT7: NavPVT7,
  UpdSOS_Ack: UpdSOS_Ack,
  EsfALG: EsfALG,
  TimTM2: TimTM2,
  CfgGNSS: CfgGNSS,
  CfgNAV5: CfgNAV5,
  RxmRAWX_Meas: RxmRAWX_Meas,
  RxmSVSI: RxmSVSI,
  AidALM: AidALM,
  AidHUI: AidHUI,
  NavVELECEF: NavVELECEF,
  Ack: Ack,
  CfgDGNSS: CfgDGNSS,
  RxmRAWX: RxmRAWX,
};
