'''
Baconian.py

In this training challenge you have to reveal a hidden message inside another message.
It is known that the message is hidden via Bacon cipher.

Again the solution changes for every session and consists of 12 random characters.

Enjoy!

reference：http://rumkin.com/tools/cipher/baconian.php
'''
msg="BaCoN's cIphEr or THE bacOnIAN CiPHer iS a meThOD oF sTEGaNOGrapHY (a METhoD Of HidIng A sECRet MeSsaGe as OpPOsEd TO a TRUe CiPHeR) dEVIseD BY francis bAcoN. a MessAge Is coNCeALED in THe pRESenTatIoN OF TexT, ratHer thaN iTs coNteNt. tO enCODe A MEsSaGe, eaCh lETter Of THe pLAInText Is rePLAcED By A groUp oF fIvE OF the letTeRS 'a' Or 'B'. This replAcemeNt Is DoNE accOrdinG To THE AlpHaBet of tHe BACOnIAN cIpHeR, sHoWn bElOw. NoTe: A SeCoNd vErSiOn oF BaCoN'S CiPhEr uSeS A UnIqUe cOdE FoR EaCh lEtTeR. iN OtHeR WoRdS, i aNd j eAcH HaS ItS OwN PaTtErN. tHe wRiTeR MuSt mAkE UsE Of tWo dIfFeReNt tYpEfAcEs fOr tHiS CiPhEr. AfTeR PrEpArInG A FaLsE MeSsAgE WiTh tHe sAmE NuMbEr oF LeTtErS As aLl oF ThE As aNd bS In tHe rEaL, sEcReT MeSsAgE, tWo tYpEfAcEs aRe cHoSeN, oNe tO RePrEsEnT As aNd tHe oThEr bS. tHeN EaCh lEtTeR Of tHe fAlSe mEsSaGe mUsT Be pReSeNtEd iN ThE ApPrOpRiAtE TyPeFaCe, AcCoRdInG To wHeThEr iT StAnDs fOr aN A Or a b. To dEcOdE ThE MeSsAgE, tHe rEvErSe mEtHoD Is aPpLiEd. EaCh 'TyPeFaCe 1' LeTtEr iN ThE FaLsE MeSsAgE Is rEpLaCeD WiTh aN A AnD EaCh 'TyPeFaCe 2' LeTtEr iS RePlAcEd wItH A B. tHe bAcOnIaN AlPhAbEt iS ThEn uSeD To rEcOvEr tHe oRiGiNaL MeSsAgE. aNy mEtHoD Of wRiTiNg tHe mEsSaGe tHaT AlLoWs tWo dIsTiNcT RePrEsEnTaTiOnS FoR EaCh cHaRaCtEr cAn bE UsEd fOr tHe bAcOn cIpHeR. bAcOn hImSeLf pRePaReD A BiLiTeRaL AlPhAbEt[2] FoR HaNdWrItTeN CaPiTaL AnD SmAlL LeTtErS WiTh eAcH HaViNg tWo aLtErNaTiVe fOrMs, OnE To bE UsEd aS A AnD ThE OtHeR As b. ThIs wAs pUbLiShEd aS An iLlUsTrAtEd pLaTe iN HiS De aUgMeNtIs sCiEnTiArUm (ThE AdVaNcEmEnT Of lEaRnInG). BeCaUsE AnY MeSsAgE Of tHe rIgHt lEnGtH CaN Be uSeD To cArRy tHe eNcOdInG, tHe sEcReT MeSsAgE Is eFfEcTiVeLy hIdDeN In pLaIn sIgHt. ThE FaLsE MeSsAgE CaN Be oN AnY ToPiC AnD ThUs cAn dIsTrAcT A PeRsOn sEeKiNg tO FiNd tHe rEaL MeSsAgE."

lower=range(ord('a'),ord('z')+1)
capital=range(ord('A'),ord('Z')+1)

dct={
'AAAAA':'a',
'AAAAB':'b',
'AAABA':'c',
'AAABB':'d',
'AABAA':'e',
'AABAB':'f',
'AABBA':'g',
'AABBB':'h',
'ABAAA':'i',
'ABAAB':'j',
'ABABA':'k',
'ABABB':'l',
'ABBAA':'m',
'ABBAB':'n',
'ABBBA':'o',
'ABBBB':'p',
'BAAAA':'q',
'BAAAB':'r',
'BAABA':'s',
'BAABB':'t',
'BABAA':'u',
'BABAB':'v',
'BABBA':'w',
'BABBB':'x',
'BBAAA':'y',
'BBAAB':'z',
}

def bacon(msg):
	ba="".join(['A' if ord(c) in lower else 'B' for c in msg if ord(c) in lower+capital])
	return "".join([dct[ba[i*5:(i+1)*5]] for i in range(len(ba)/5) if ba[i*5:(i+1)*5] in dct.keys()])

if __name__ == '__main__':
	ans=bacon(msg)
	print ans.replace('x',' ')
