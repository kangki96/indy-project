import json
from indy import anoncreds, wallet




#proof= json.dumps({
#        'nonce': nonce,
#        'name': 'proof_req_1',
#        'version': '0.1',
#        'requested_attributes': {
#            'attr1_referent': {'name': 'name'}
#        },
#        'requested_predicates': {
#            'predicate1_referent': {'name': 'age', 'p_type': '>=', 'p_value': 18}
#        }
#    })



vp = {"proof":{"proofs":[{"primary_proof":{"eq_proof":{"revealed_attrs":{"name":"123123123123"},"a_prime":"7646995952123456912527850836758733237898400732618802243559638810896386383162951088888206950108830966506124469631956175346450632796678218118219904614361126098866812285314946808696769228070186420263185086127342401867723812083877213676551356194926822367532323696537872903195783282303469058917318836196788994553373210539279267558920576786972019290557364038026558636499546104224358758791864851167063519845008967528706247869418584192333145190210362611339410890234257382160633443338271964693062729019900170270507321747177061854757778788198023927752755201467623875564905428310359939264757947476846281462036476812502831267028","e":"119787890454420105062655602380055918486038398527849532884824072183258009922951735242979837933065546848415275462082891991450695112320168168","v":"838201687944556482036231691930986295971969559235729980377737072227406195414739632761262011254999371937848916256000937364826156132753675570915819055347478056345016727706991427173244364331593818409529930234749479743889307438142861353133981943205078198330631185583228234227145003590900501064289575552239716685997459354138909314812413748289932752460349355634516560927297103260767657436939808187865179093067868553580618889669244234615900870480367071883989438232141840847528641504708691029244992615772875608574719550321891466218219003209082005127958955646981657528672060953946160657726041108185899166193051808927206774542481296689446980080072376530568266135683915288404609083111683567855198356782077765823435784399935016755479745061396575686839871216495678273916747578920651227206860654808533920639369361766399089886470885216849965537203843104061416835446580669767275163829181376536849131851321670021667402370284648815889779056","m":{"master_secret":"16079834002087280529899556550315354549896162495965869475272617287986656773828232247695000097943199506201198152161351099141726119793854886163754018204116023289874101092932215640714","gender":"5455701376606934808492063238774236615410111538139112706000519098340323949133452397199551441905813683243132523433903489377403493839890139718068064261406873905092554436794075204368","phone":"5710354436689340981789043758843987133828059747950584904706773987784230646549244112522263036802627476485019691312236069879420060378358209437139682489167120874460933198378800436787"},"m2":"4210046714772743705145334279742453431514136323956276648328586775076171108043885598162623707620503632922130125030333837558818181645231135902294033342866139387178936465802143233545"},"ge_proofs":[{"u":{"2":"945227365320869557516357505150529192400313927023713877209724049546677060561874462371084493324622182935040098834888294391871590837647783107857400388358943195058972935342119927075","0":"1980235611849215661821635884764654004407387673865272158134404287814256549475229897928706275507728557043099577958335286942417218757174534820220144241423919104256905823408250912923","3":"2628066325964153899905708880738313648985250244906533072177454614812762216881461391911579264466932853109606537230579279030911221312759479329904052021341167807239414582691043070022","1":"11943385578323918970709886389306878514834218884399825839414323737939130054469514621900410767819674252188040847289292460959094968679289319051740673306860705642583729365127290206287"},"r":{"3":"2490160607201799942182425398306024401115184426896967631457750992604849790655612609537778667388260130331861721609865602255828390823375657202333351029092688531079343364271711958275517581560216537932204622715366288705304986948772344431443874718995121491108683769652977315355717134943161514772090272969759120325103493182714508127936232128803876656305145247012151192847205953445661935626715182799410794691040137858107111393607184459394551447906948547400796532444757265417883266825401966938698587900385038677730137822550343453776307577768189629658265478130885342890600853086437117880183546215494788443237027382731954338854759680611776127597245662652298471546571107030890118413147541561916781359924620253898760855073772270381","DELTA":"1788543807314605042165241627403730499895602515610034118206572312675966189374018738903820390448431827150792321371700351563319429366767009457530320244505967465961473982303887966108977010671879510161418476095990948120838088260978111571499565520640180437466830227619472379300893038843508862025789391320593846580533522723147735907763367115693512471217458556362283352396451502512400368141437970025662868103025324624585921953552391142862097993999117924986060861432466285718653894153773787987110193631833714499642258180413718038766293489663965748112046926914251635218050263587061397796627500284527050915402967485532897575819771311273650434186592381872344440970021528165999256714966800927088076335451883849848296441490566524992","2":"671147045109851858886422492167309652770230437476063085120726298598304703524164411787006444026388574509919354016779515058929814872437475693640905265454013100773630387791622780989283547374326283439213582040940909967677951091369794488890244610804745701289802645294533501688820927063362848565280117168906875235283353682852199785643099910235636761891491172590660561792337711257301116767572576776233297958435802376699384113459196611636222458539133488977374645439145489596199278870807025853183582917243681592796888836957574459924622445656667761398710414205283317766831011477740977206181808064804970056013172271112955722629780531507027219153251037548345202576205611586740914053486331610630290255204691238024169618043470964738","0":"876845476811008721346340455540832211868564465438308076528398130039875851229543884272353739308266283962666039407723286219884838868979217505538856077616614621656491554161296661687946812351920423129220028849957728571790349212785262632525081432470560858730087135030337745286253175086527418137170771857077721229779960629346920596264758288450678009705911904642745300856216953353310509475409098999974538954575145775845115452187289446678298165583765686410648255461319456251253486351126568403160253937856224693752851574770651449823398072834005932966808048482257423654953336964362783437543075556058161007280579898289890113437741323055303116240872174172285290276448910112616955553585574616326844926906438192406819444264538862960","1":"209587016852461238252965268154534345232720583548712309641689433526067157293070944585201225917138204693659093040171489255241626942750143459131969147093887441441060501788669068955835860377340900096694943715772961462557682298867583303435608248072890984255075682079402347722141762691019032074503475032269560155851745647299260645437535444131234138682507177157542888286642948035926087825135763940201328718555185173825788244076892458994455285737623918529303220151969697009968332173447359118271782588638103665577906310143261716595735474696216392390156037543923515247018566258080443113552779541519751625882987000913375540899632563233243458186008524474890036437109592242766042376604165708876564395000297062217819261640921542364"},"mj":"5455701376606934808492063238774236615410111538139112706000519098340323949133452397199551441905813683243132523433903489377403493839890139718068064261406873905092554436794075204368","alpha":"30667337407624313159258251022826434128221522250346792612114101569769325642885340738428598974734207010839297082129742862714461459916639670394600837501431261038501873609648039229814069298565395149253716761582183250460586874401414569383289873377599006586171920539994169993189742046267403576478141301878411775742925708094722948357529090803228395131791868838284247065898509391660350130934545172459910509947531422757339669692770807348549856096771562590532683822823640786776391303309022640233855452421555607401191847339074017288002099795416586424636276790999769185058757958284761302169425043587636538386857563779864901502999093636486272195672005762533616392842883638665167283157752354243176930448146694732205790405778764749671783687623502699413162321837661100438834979774414604745381243656351162492056428590857303290483538960670097795235509959597","t":{"3":"36294809212575004280250972438825714577037986680331619164851141964902384107727243573397618905760837456304939304584116883179391273047125575941382557302943000373998592116252102545964067808106243118378404609611833030288084210867940052776475108126774311303045529452252029883428946058489047186734920478795472394913423540692123959947630367437415278921953458641034901495211092930156885953329149281619187695166215881532070482213118106130564930337686720765092915852977218175728958003513850522499106259309194073540932084116045530741031495115223665026227598542371228947018291001403579116469843953686722217874253225329687317621264","DELTA":"44615710255007019506121589316170711691465177173458392292801672476179010137269603221357295843011238013379409008783229601268904384477405219535963574787090156872574551126479307691009981054079774679178985081434374305819772873379131619735056065082555133081065033901928934820466354240552638487005347773803440661716222614156140201260972615661705813422949678424641218967242192810798469889941252939808196563248511263313018152470043021587391871342407111033286887011220619081690950098274326385690501289891056581324084490658219681492629629741439613257478022668111764536666991188876435081930135978152552457933201840466306124504395","1":"52996844686373729214518264394093599531047622930842594933668125928629866099600507177165243112250326481823549558773945073632691667368068666243032431026447956749513170163853196635965039777370780226897218555259197221837075788924227646256531938797410950752440052845400228298580389043062896689608095822738849009460013315298042771086526498630252953795194693104605098969317963362222156758009956972275736380734660311037395584667534208386000439800061480673142820917576718928841571379036308194141637122031464549918849969461331546499900521737073087061798098959743342377331320891723586914571768548740734490582613612924571268483164","2":"78957341775911842249481842510116736600137719515910122284733454430659175875613047483940149534419911618862463780235627788463037441377935666689489667643561341247263399737705538802938109757101240145008506871915703978207581438959004009525221487376780970126520729533148924350692531804656419712994069697850645052055041397119400561442692194876176811034033152986772961798830398722649083096311076113541951465517799236070822698917344658088956385544624393007490609067329592201825810822048984308305643665363165494871675713296545798390744837056971834183719515643655282403446092113550920040360678250077398365072839348779232534044728","0":"81973254726628687378923038770339722102318699177554441846429757519888692337618647702886719985493990563359627065474029652228705500448810344917693940066640594346397441958990362626611612881419796868700790791969499180396975443774059426337122193066826798796373822773682947211988608107546553959814774191896957166845330780199893632019685893734565368002091677004604007804625458089164180073057884780038952948897226192064425988124638897209162083415559047734626215800091686315157461374864368560490002571635846279100017094575591561928320840951299113688832075007383171715900863293514074346957891318030579541344125795770701746943349"},"predicate":{"attr_name":"gender","p_type":"GT","value":99}}]},"non_revoc_proof":null}],"aggregated_proof":{"c_hash":"100621016148723262103378245165795535372140889934796823870194308730787597915917","c_list":[[60,147,108,161,229,58,52,194,239,10,102,114,101,191,254,123,89,91,36,195,161,200,107,174,107,163,96,18,251,158,193,76,134,159,52,170,176,200,136,118,107,216,254,71,250,230,61,121,88,225,165,3,60,139,79,56,0,14,101,70,125,136,94,115,123,154,232,5,140,77,135,249,123,14,93,4,76,221,10,151,66,210,173,38,75,24,151,153,15,188,73,234,56,78,1,88,237,167,11,147,3,41,60,114,153,58,206,231,70,110,180,14,18,0,160,80,79,224,246,140,128,181,31,111,175,179,174,18,66,142,146,17,4,9,68,188,100,145,28,156,159,169,200,230,199,214,47,184,37,27,225,196,176,90,135,140,180,249,177,227,142,41,168,185,93,106,173,59,213,34,136,8,231,77,136,86,188,99,42,179,8,145,42,105,118,43,162,217,43,122,27,4,149,121,82,233,44,191,131,77,7,175,170,73,37,77,253,10,8,75,28,62,78,191,99,112,165,76,85,123,225,185,135,26,59,243,148,7,90,187,225,202,118,203,178,19,137,129,53,144,229,112,4,57,111,240,0,92,203,158,96,198,167,136,252,212],[2,137,90,111,44,185,80,229,83,4,215,178,237,95,117,108,180,162,199,197,175,227,115,114,61,20,72,60,74,201,163,25,213,70,144,108,106,165,119,61,249,213,54,184,71,247,180,114,159,140,64,197,196,206,73,9,91,14,246,34,195,150,188,15,62,66,182,110,194,174,109,79,50,16,186,206,180,143,6,201,107,174,241,213,128,51,167,117,90,159,159,82,198,72,90,208,106,184,161,239,46,223,235,71,227,205,177,117,176,36,59,155,248,227,4,158,31,178,219,178,95,65,242,211,127,183,3,12,140,91,196,6,172,120,65,11,151,14,248,145,187,19,67,246,16,13,206,246,137,151,77,36,90,155,28,115,93,35,210,177,72,235,10,232,100,54,30,227,56,187,33,24,243,118,188,249,222,43,236,229,30,62,27,76,216,32,243,93,192,67,81,195,137,111,66,45,90,4,12,58,71,74,177,140,229,52,236,67,118,15,104,239,28,169,195,128,1,72,167,9,57,212,110,18,13,89,102,177,207,166,190,251,125,211,34,184,159,218,250,176,218,33,33,181,13,85,98,93,113,86,147,81,214,8,30,53,117],[1,163,208,221,77,121,221,37,134,0,49,75,15,154,43,78,201,114,249,236,225,185,68,80,230,226,215,8,22,238,77,233,64,218,102,215,141,253,18,42,179,77,148,70,86,59,51,176,8,103,41,77,241,252,133,201,24,8,26,42,80,154,15,222,51,190,248,47,127,30,97,116,139,134,21,172,12,200,85,111,44,142,141,56,174,126,134,6,195,190,208,232,83,55,113,122,17,151,49,42,171,181,57,30,126,83,203,107,246,132,70,2,197,7,27,172,75,106,191,2,85,29,217,85,2,17,28,97,151,94,93,125,111,151,168,124,184,217,207,68,81,75,255,94,84,214,98,37,134,124,90,149,111,60,62,34,207,188,252,11,41,28,136,147,97,242,58,11,17,116,10,166,23,129,67,74,67,174,24,88,127,7,237,154,15,106,238,34,159,112,87,23,172,65,230,225,208,44,207,76,10,6,125,133,77,29,176,44,205,190,74,152,151,107,166,59,142,134,116,118,83,249,6,150,27,99,192,150,154,10,7,207,103,21,233,43,193,49,75,76,103,179,91,182,11,81,132,153,19,253,197,7,46,188,197,8,92],[2,113,118,110,174,251,46,175,240,204,252,117,174,36,27,147,6,62,4,44,91,26,149,159,174,69,33,99,71,239,82,97,209,39,238,207,44,128,64,66,22,104,242,53,232,168,66,1,28,226,54,28,103,3,178,117,157,21,8,91,99,240,106,88,152,143,142,33,197,91,21,99,95,159,182,66,246,144,92,28,212,161,189,44,4,207,114,251,209,227,126,7,248,238,44,19,48,197,72,186,161,211,22,152,201,108,8,90,240,44,34,32,70,46,157,170,201,155,152,104,114,169,157,103,197,178,48,67,90,21,130,77,27,253,6,111,16,132,80,244,93,190,133,153,32,75,10,88,56,136,54,127,201,35,205,170,193,197,215,165,57,127,199,216,136,232,163,85,78,123,82,63,153,252,185,31,127,232,34,114,24,142,69,182,232,100,2,119,244,123,103,80,62,5,69,252,33,82,29,202,86,93,139,230,187,162,170,249,229,250,255,21,213,10,20,143,9,109,35,172,50,176,245,17,72,95,77,205,46,149,160,133,72,156,36,83,196,171,162,120,169,169,77,61,205,247,59,153,100,182,88,80,101,230,245,160,56],[1,31,130,161,22,248,168,215,57,11,185,54,119,118,208,183,36,84,43,79,3,34,100,123,20,250,204,122,221,240,14,24,181,48,243,112,204,35,150,187,161,108,151,191,206,2,90,203,241,254,231,62,47,139,70,141,233,138,128,187,192,231,41,166,200,1,112,212,122,27,44,39,205,39,204,97,83,206,251,235,199,58,185,237,48,255,82,149,87,72,14,207,220,68,3,51,179,254,225,157,183,246,40,161,199,222,206,208,203,70,97,69,39,40,76,244,60,93,42,180,180,101,47,49,212,189,96,193,157,98,156,74,170,38,124,220,125,229,249,208,131,70,72,181,247,137,145,81,191,100,120,225,204,35,165,175,72,30,199,39,163,252,199,0,153,141,121,130,56,60,103,113,31,255,135,114,53,163,124,183,221,135,62,34,49,149,165,195,102,135,176,185,0,212,250,172,227,61,225,253,5,122,229,24,78,8,76,122,212,236,238,32,230,30,56,103,86,210,154,223,201,142,25,20,156,14,99,144,138,112,248,154,70,72,105,20,106,91,54,194,78,167,209,34,89,91,125,43,163,102,233,162,147,230,254,170,16],[1,97,108,172,66,223,51,71,36,173,28,175,175,152,125,244,58,3,180,52,83,90,196,53,140,186,17,199,133,204,219,209,123,63,236,125,204,154,153,125,63,203,0,61,219,117,79,213,96,174,133,8,243,99,118,70,98,238,96,231,137,4,120,155,158,90,232,20,219,245,85,63,24,252,37,215,163,81,235,57,243,236,60,186,200,105,222,76,96,147,175,22,99,88,120,19,232,60,75,31,224,42,17,223,128,198,243,106,153,217,102,45,181,1,89,198,189,57,210,44,111,57,85,88,246,67,19,166,152,204,118,78,250,211,0,50,223,74,214,207,62,63,219,146,9,168,195,138,103,14,30,184,136,164,118,219,172,36,93,85,45,219,197,154,242,83,95,105,86,121,238,113,92,107,175,209,240,64,213,255,236,158,24,203,221,195,85,188,182,195,247,62,243,196,83,223,193,165,79,113,173,245,104,95,116,64,16,163,250,213,196,41,49,199,131,26,52,217,99,237,140,218,191,111,26,30,99,110,81,103,230,223,18,116,26,84,249,203,84,226,189,174,98,27,27,249,95,220,39,112,83,62,28,121,224,93,75]]}},"requested_proof":{"revealed_attrs":{"attr1_referent":{"sub_proof_index":0,"raw":"junhong","encoded":"123123123123"}},"self_attested_attrs":{},"unrevealed_attrs":{},"predicates":{"predicate1_referent":{"sub_proof_index":0}}},"identifiers":[{"schema_id":"EYYre24MSmo3tQwC9S1YWr:2:toilet:1.0","cred_def_id":"EYYre24MSmo3tQwC9S1YWr:3:CL:EYYre24MSmo3tQwC9S1YWr:2:toilet:1.0:cred_def_tag","rev_reg_id":null,"timestamp":null}]}