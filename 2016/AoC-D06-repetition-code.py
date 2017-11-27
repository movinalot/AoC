import operator

repetition_codes = ["cmezkqgn", "nmzrgcft", "ydpndcps", "zjihhows", "kvptxsrx",
"ubbvugwq", "pclcquhl", "rtddzpes", "gfkylkvo", "cpxpjjme", "qqntjofm",
"tnvmqrik", "cczmxxag", "ikbrgpjh", "lpeohbro", "sgdidbgw", "apjhovfs",
"miwqgpmr", "igkccbxe", "dcfpfkdv", "neaxgnpr", "xjlnhgwz", "hbwdbtmt",
"jaahaztu", "xdhkxiwj", "kbcnydre", "zygzcjxg", "pnhlsbyu", "gpkfcakg",
"vlpebsme", "fhivcwnn", "avscujyu", "tckpnxnn", "vhtaizda", "vghhmhuy",
"dtzhrwcw", "qhbcdaxx", "kdoadrvh", "yrjzipbd", "weqfqmqr", "zlkaiefc",
"zziwfitz", "hfdvzpol", "opialtmr", "wgbarxig", "gguytyxk", "gwvaqisb",
"vybedyip", "cbcdebwm", "twoqbnis", "itrspsmt", "cqvjpfou", "avhpvkbz",
"xozehrwd", "qizmzubk", "hpyiulwy", "clmrwgdt", "uruutjhx", "pyvkmpxk",
"wpjfzzst", "hjxjjkup", "mdtlnvab", "tqwnjufv", "nlaxmbxc", "nyetqfpn",
"nmapoequ", "aozqvnbx", "awuopxxj", "jjamjzdr", "xsgnpwrv", "odpbdulf",
"nnpddykk", "fwkqbeeq", "rmpyqcrr", "nnrbqymd", "advolplo", "xfwzojqb",
"dlxozmgp", "mehtypai", "qgxmpmza", "cyflmzcf", "drilfbik", "hsrkwohm",
"lzdcksvs", "xtqiuyon", "aatvfuvn", "tgdwdznm", "srlndtlz", "kcdtqqov",
"rjjwcfpr", "sqmwnyjj", "spfagdkw", "ffqrocvz", "fdncyaef", "doymrkhy",
"nagivkzc", "ylvmvlvo", "yqnpiqnx", "yqiuccji", "swugswxs", "wlfcvtms",
"bplwnlqh", "dyqqbiop", "ugxdfwnu", "actfbdnl", "hafvcdjm", "uxlvddgb",
"jimpqraf", "oovjqvmc", "niixikhh", "uamcczvl", "iqyhtphk", "hmgnaqfa",
"anptkatn", "taslmdqh", "hrsdlgth", "tidxkojm", "bozyplbl", "viyiykes",
"bqttiowc", "fdygoexj", "yxiqrabo", "hoqmzyap", "qrdjlssb", "kpoknmcl",
"wmfbbpoz", "xyfmwzrc", "ekgikzyt", "furxwelu", "gtfoyquj", "xhtkpgnb",
"pqwfaoeh", "kgutwopd", "gmsrhxhp", "yfriofga", "kjulfqdc", "anyrvwxv",
"reuufyff", "rhhuhyku", "muwxqimh", "lmmesfgq", "buklvija", "nrqemlud",
"waggxokb", "dmmtiifd", "kgawgnsa", "pvwrwdhz", "mboaagdf", "tugpycjc",
"yrrurffl", "xnpptcxi", "wynqznnj", "pecxtzem", "qsmjkvvd", "gbosyfyx",
"dckxdlle", "oyuucewm", "rvzinbwp", "bwdsapew", "qacnmkst", "dunstuov",
"gfrmztat", "psehmndx", "krhyzbag", "trxayqjv", "ddhrarzx", "msnjiwaf",
"znjklkrs", "gzhgcuqn", "eoivvakl", "ekjbelae", "oxvbtsmk", "mwfqyskr",
"tihtgxtf", "hldkxeuc", "nnawdxvy", "euemeepz", "ibnuhhex", "ojwihmnv",
"cfpezewj", "vrxjrwia", "wgmyafnj", "pnrsmxka", "ksuwbzlt", "uwkupngv",
"jdajpsal", "tbufcuza", "jjgptlxn", "hxoulqig", "gieqsttk", "fwjyxnaq",
"pmfdifiq", "qcgjfmsh", "bnzqevtw", "zlosluzk", "pyfrslkb", "ivzxjsgx",
"wahqmige", "uhvsplzs", "qaatujkd", "taryjkox", "jwdwisfv", "dtwhlvuv",
"lwlwbjee", "wopsiktn", "iojihkrw", "pwmqgwpk", "kepvgmcd", "dqgupbhg",
"srofdewh", "ntijingz", "osixtaku", "isacbsnl", "txtaxccj", "uuqanmcw",
"nsuogfzt", "yktybcsy", "csqjvxog", "rrjygfmc", "eftdwemr", "uxbswaep",
"zghswtrf", "fhlxbray", "julloyea", "bsxwmvfv", "kzatuvcu", "mnymrdpq",
"idejsnhx", "kdbpzapz", "tzjefanj", "ottzlwxh", "mifokhqj", "lxxbtzjr",
"wjcblnsd", "siiozsqc", "iujapalx", "ofsvvyuy", "zbgpxvrb", "aqbilxlp",
"ncobthcc", "sflihopk", "pxwtiwam", "nmgzdpyj", "nhjhaezr", "weihbqyp",
"pkpnbhxp", "dlrelmop", "mjbvnjuq", "qntmdrey", "htiluzbi", "fingzxbe",
"mnekisyu", "ynfcmhzd", "vdzoljfg", "wfmscpvw", "efvyjhux", "gvfkaxjq",
"rkmkahxl", "vhqijllu", "kkjpwxlq", "londfadk", "ohsxywdq", "znstqcbb",
"qtazxfoi", "jdqwiadz", "mumicrid", "uhwfytgm", "srqofgqp", "gtlqqspw",
"kxnkrcln", "aycqjkay", "yvangrcm", "tpokdbwt", "hmfqugbw", "qoymvotr",
"icjendxu", "uqsvumij", "bqkqoeul", "riarnbdv", "zwlltddu", "izcmngof",
"lawuhjjj", "fdtnicju", "iizykequ", "lwrfolub", "rknrbikc", "yvogoydm",
"bogzdkiw", "obnhuoxn", "lzzpupsk", "nuefyzzr", "azghigtg", "mkyduyug",
"mnteeioi", "yhqbtwyx", "eaojxpwy", "hbbxehvr", "omdkihmb", "hbcijcio",
"settptzw", "babyhhhe", "cdlexgrs", "cwrdtzjk", "xvtwjacw", "lxeykife",
"szogbxgb", "ggxlgisl", "kbmrnfro", "ioervjsx", "pfkodypz", "ojgbokwc",
"jvykzhzc", "cmigvhio", "wwiowvyo", "igwtrxhe", "obawztja", "yyazfxks",
"gfqqttue", "czmvgttl", "aljlhlyo", "zczpqnzb", "ruofwgrx", "bhemgvlr",
"yzsulgck", "eixzpfkh", "cbejkdrs", "qcsnnfht", "ryvlmbiz", "nfswleyf",
"xtoxoitk", "ysfgwpmy", "zsnapbrq", "olqagygt", "zmtyqfvd", "ztybusgn",
"zsydzdnl", "fkbvfvsq", "gwdjudok", "juzbnhfe", "apivbufk", "ozxgeeqa",
"yvyvuvxh", "kexcesza", "gqefjmed", "hqyolehg", "mluggzqh", "gkpjfkhg",
"bmvxtrci", "euyduveo", "avwdogys", "jnserfgo", "iysfpsns", "nxilicng",
"rpclnuwl", "anxroxpu", "fjmenahn", "xngxqxxt", "ziwltmcm", "rdizrucj",
"wvvwldvq", "blyiqvpw", "iklfxllo", "txueozfv", "wapwemje", "bztthavf",
"fkfejluf", "iwynejes", "mkwpylhy", "pmndxgby", "vhgdvrbv", "fizshysy",
"phqddggq", "bosaehqz", "kwsoncrz", "pmaethwo", "valgeqbq", "rcjuatfg",
"ryaujqvn", "urpgwdyv", "gdefrqbu", "jcpfzans", "eywcyjer", "xpkacpyo",
"xqdukuff", "lmbaxfqi", "tzvnhfms", "osqfwpss", "ltgvoipl", "bcorqrzk",
"wgccrykp", "aaaoczvn", "jpbsehyo", "qtfzphwh", "bpiiwzib", "tnxbnwyg",
"xruheaca", "eoxvahaq", "dzhcleaw", "vwcgptbp", "mmqzjwte", "gpxrndsm",
"kdgwktpb", "roqqxgvt", "tceymtaf", "pkelkvvi", "jqfguroe", "xbrhyuai",
"jvbizlbh", "hhujmghp", "xxtagkzc", "pxtzfvsy", "vlopcrko", "lorhgtfj",
"eyuzxpjt", "jxjbdzrs", "jfcuqypt", "dcmbqqln", "stdmubrl", "fkvvwbue",
"mqqhkoqd", "lvmnavnr", "gtxksotd", "dyjdydhj", "rknodxpp", "nkrbeqgp",
"lzzlxjub", "hfhycqag", "zrhtmjcz", "tetkoiki", "aeicawds", "kvverwcb",
"vkkmanit", "ozzoauql", "eqjceipv", "vjeajvzj", "rfbyfkdt", "ayudrwvi",
"ozlumnku", "bbmgldja", "dwpjacmb", "ddyqbnzl", "jlrdfzef", "quovmsbh",
"utposqki", "howsfhba", "rdddsgwx", "fcdtcqni", "kbhnvmah", "cgpbjquu",
"qjhmpyff", "wxkytidy", "ssefidnf", "opswmrqz", "zhcskfsp", "hhkqbfon",
"uvgdhifc", "eoewusji", "xjmylrdx", "fabeoujy", "gzrceopo", "fxsivztv",
"veqxwblf", "sacoxlhm", "xongcuef", "lufmhuoi", "juzgavxq", "jjwlcfjq",
"egmnqjqn", "ryhlipod", "uagzcjur", "epjngrwa", "fijrzmww", "zihnvpgp",
"zjurrctz", "irhnbjjr", "mlrfavaa", "cokssyim", "auwsrcsm", "wrkkttyo",
"cmskryli", "mrkpezgq", "ehefyaqv", "ivsuxdll", "gscbkguh", "bfxberbd",
"vihesdxg", "vdbxzltv", "lkoiranw", "qcnefblb", "cfftjwud", "xqpieetw",
"crnrywvn", "eepxytfc", "cacfhgnf", "bakhanwy", "lsnlnmrj", "usaurokx",
"sjqbyile", "lvcgmrte", "vesupotm", "yeusftiz", "clnjmcit", "jhexzuyh",
"wtbiuozi", "fsnqljcg", "fxretbsa", "lsagjnhx", "jjknskzr", "dllskstv",
"vgxhdbyw", "yryqoqgz", "ycilkokz", "vfdcsamh", "oedmwosl", "vzwfymbu",
"eqrznqgp", "fevhvwom", "qextbmed", "ubdsfkiu", "stvuqrka", "nmcrshqw",
"zlfzaxmw", "qzcagqcq", "djudatbg", "usknomtt", "busciicd", "wyugburo",
"qblpvrxc", "shzawivm", "ztgzrklm", "ahpxtdmz", "obvuhnlj", "uihsumey",
"mircsnyv", "ijjhkyjw", "dgxmzhgq", "rqavgasa", "lelkschr", "svzzvroa",
"sevzfvbh", "kgzcpbdj", "wvctsjcp", "kgdrxolj", "tlsksbdi", "ycqvhidx",
"epcaeqir", "xcrgjgzi", "snuvvmmy", "cxbxoxvb", "leykoxno", "ppvysjob",
"eubrylie", "pxspjeqg", "xbdesmuq", "bfcpktpy", "elyounyn", "niwhwuak",
"hukkheui", "ueojrjoc", "mktpkpsk", "uxljxoei", "hymwnsrf", "sgyywcqt",
"yznoeeft", "puvcmnpe", "domsvurc", "ukbhxndd", "qwlzklcm", "qttwpwdc",
"vxljmley", "sjlbsszg", "iqobsomn"]

#repetition_codes = ["eedadn","drvtee","eandsr","raavrd","atevrs","tsrnev",
#                    "sdttsa","rasrtv","nssdts","ntnada","svetve",
#                    "tesnvt","vntsnd","vrdear","dvrsen","enarar"]

letter_frequency_col_1 = {}
letter_frequency_col_2 = {}
letter_frequency_col_3 = {}
letter_frequency_col_4 = {}
letter_frequency_col_5 = {}
letter_frequency_col_6 = {}
letter_frequency_col_7 = {}
letter_frequency_col_8 = {}

for repetition_code in repetition_codes:
    curr_col = 1
    for c in repetition_code:
        
        if curr_col == 1:
            if letter_frequency_col_1.has_key(c):
                letter_frequency_col_1[c] = letter_frequency_col_1.get(c) + 1
            else: letter_frequency_col_1[c] = 1
            
        if curr_col == 2:
            if letter_frequency_col_2.has_key(c):
                letter_frequency_col_2[c] = letter_frequency_col_2.get(c) + 1
            else: letter_frequency_col_2[c] = 1
            
        if curr_col == 3:
            if letter_frequency_col_3.has_key(c):
                letter_frequency_col_3[c] = letter_frequency_col_3.get(c) + 1
            else: letter_frequency_col_3[c] = 1

        if curr_col == 4:
            if letter_frequency_col_4.has_key(c):
                letter_frequency_col_4[c] = letter_frequency_col_4.get(c) + 1
            else: letter_frequency_col_4[c] = 1
            
        if curr_col == 5:
            if letter_frequency_col_5.has_key(c):
                letter_frequency_col_5[c] = letter_frequency_col_5.get(c) + 1
            else: letter_frequency_col_5[c] = 1

        if curr_col == 6:
            if letter_frequency_col_6.has_key(c):
                letter_frequency_col_6[c] = letter_frequency_col_6.get(c) + 1
            else: letter_frequency_col_6[c] = 1

        if curr_col == 7:
            if letter_frequency_col_7.has_key(c):
                letter_frequency_col_7[c] = letter_frequency_col_7.get(c) + 1
            else: letter_frequency_col_7[c] = 1
            
        if curr_col == 8:
            if letter_frequency_col_8.has_key(c):
                letter_frequency_col_8[c] = letter_frequency_col_8.get(c) + 1
            else: letter_frequency_col_8[c] = 1

        curr_col += 1
        
print letter_frequency_col_1
print letter_frequency_col_2
print letter_frequency_col_3
print letter_frequency_col_4
print letter_frequency_col_5
print letter_frequency_col_6
print letter_frequency_col_7
print letter_frequency_col_8

print max(letter_frequency_col_1.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_2.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_3.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_4.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_5.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_6.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_7.iteritems(),key=operator.itemgetter(1))[0]
print max(letter_frequency_col_8.iteritems(),key=operator.itemgetter(1))[0]

print min(letter_frequency_col_1.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_2.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_3.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_4.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_5.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_6.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_7.iteritems(),key=operator.itemgetter(1))[0]
print min(letter_frequency_col_8.iteritems(),key=operator.itemgetter(1))[0]
