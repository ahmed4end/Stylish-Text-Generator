
text = "hello, world!"

letters =['a𝐚𝑎𝒂𝖺𝗮𝘢𝙖𝒶𝓪𝔞𝖆𝚊𝕒A𝐀𝐴𝑨𝖠𝗔𝘈𝘼𝒜𝓐𝔄𝕬𝙰𝔸',
		 'b𝐛𝑏𝒃𝖻𝗯𝘣𝙗𝒷𝓫𝔟𝖇𝚋𝕓B𝐁𝐵𝑩𝖡𝗕𝘉𝘽ℬ𝓑𝔅𝕭𝙱𝔹',
		 'c𝐜𝑐𝒄𝖼𝗰𝘤𝙘𝒸𝓬𝔠𝖈𝚌𝕔C𝐂𝐶𝑪𝖢𝗖𝘊𝘾𝒞𝓒ℭ𝕮𝙲ℂ',
		 'd𝐝𝑑𝒅𝖽𝗱𝘥𝙙𝒹𝓭𝔡𝖉𝚍𝕕D𝐃𝐷𝑫𝖣𝗗𝘋𝘿𝒟𝓓𝔇𝕯𝙳𝔻',
		 'e𝐞𝑒𝒆𝖾𝗲𝘦𝙚ℯ𝓮𝔢𝖊𝚎𝕖E𝐄𝐸𝑬𝖤𝗘𝘌𝙀ℰ𝓔𝔈𝕰𝙴𝔼',
		 'f𝐟𝑓𝒇𝖿𝗳𝘧𝙛𝒻𝓯𝔣𝖋𝚏𝕗F𝐅𝐹𝑭𝖥𝗙𝘍𝙁ℱ𝓕𝔉𝕱𝙵𝔽',
		 'g𝐠𝑔𝒈𝗀𝗴𝘨𝙜ℊ𝓰𝔤𝖌𝚐𝕘G𝐆𝐺𝑮𝖦𝗚𝘎𝙂𝒢𝓖𝔊𝕲𝙶𝔾',
		 'h𝐡ℎ𝒉𝗁𝗵𝘩𝙝𝒽𝓱𝔥𝖍𝚑𝕙H𝐇𝐻𝑯𝖧𝗛𝘏𝙃ℋ𝓗ℌ𝕳𝙷ℍ',
		 'i𝐢𝑖𝒊𝗂𝗶𝘪𝙞𝒾𝓲𝔦𝖎𝚒𝕚I𝐈𝐼𝑰𝖨𝗜𝘐𝙄ℐ𝓘ℑ𝕴𝙸𝕀',
		 'j𝐣𝑗𝒋𝗃𝗷𝘫𝙟𝒿𝓳𝔧𝖏𝚓𝕛J𝐉𝐽𝑱𝖩𝗝𝘑𝙅𝒥𝓙𝔍𝕵𝙹𝕁',
		 'k𝐤𝑘𝒌𝗄𝗸𝘬𝙠𝓀𝓴𝔨𝖐𝚔𝕜K𝐊𝐾𝑲𝖪𝗞𝘒𝙆𝒦𝓚𝔎𝕶𝙺𝕂',
		 'l𝐥𝑙𝒍𝗅𝗹𝘭𝙡𝓁𝓵𝔩𝖑𝚕𝕝L𝐋𝐿𝑳𝖫𝗟𝘓𝙇ℒ𝓛𝔏𝕷𝙻𝕃',
		 'm𝐦𝑚𝒎𝗆𝗺𝘮𝙢𝓂𝓶𝔪𝖒𝚖𝕞M𝐌𝑀𝑴𝖬𝗠𝘔𝙈ℳ𝓜𝔐𝕸𝙼𝕄',
		 'n𝐧𝑛𝒏𝗇𝗻𝘯𝙣𝓃𝓷𝔫𝖓𝚗𝕟N𝐍𝑁𝑵𝖭𝗡𝘕𝙉𝒩𝓝𝔑𝕹𝙽ℕ',
		 'o𝐨𝑜𝒐𝗈𝗼𝘰𝙤ℴ𝓸𝔬𝖔𝚘𝕠O𝐎𝑂𝑶𝖮𝗢𝘖𝙊𝒪𝓞𝔒𝕺𝙾𝕆',
		 'p𝐩𝑝𝒑𝗉𝗽𝘱𝙥𝓅𝓹𝔭𝖕𝚙𝕡P𝐏𝑃𝑷𝖯𝗣𝘗𝙋𝒫𝓟𝔓𝕻𝙿ℙ',
		 'q𝐪𝑞𝒒𝗊𝗾𝘲𝙦𝓆𝓺𝔮𝖖𝚚𝕢Q𝐐𝑄𝑸𝖰𝗤𝘘𝙌𝒬𝓠𝔔𝕼𝚀ℚ',
		 'r𝐫𝑟𝒓𝗋𝗿𝘳𝙧𝓇𝓻𝔯𝖗𝚛𝕣R𝐑𝑅𝑹𝖱𝗥𝘙𝙍ℛ𝓡ℜ𝕽𝚁ℝ',
		 's𝐬𝑠𝒔𝗌𝘀𝘴𝙨𝓈𝓼𝔰𝖘𝚜𝕤S𝐒𝑆𝑺𝖲𝗦𝘚𝙎𝒮𝓢𝔖𝕾𝚂𝕊',
		 't𝐭𝑡𝒕𝗍𝘁𝘵𝙩𝓉𝓽𝔱𝖙𝚝𝕥T𝐓𝑇𝑻𝖳𝗧𝘛𝙏𝒯𝓣𝔗𝕿𝚃𝕋',
		 'u𝐮𝑢𝒖𝗎𝘂𝘶𝙪𝓊𝓾𝔲𝖚𝚞𝕦U𝐔𝑈𝑼𝖴𝗨𝘜𝙐𝒰𝓤𝔘𝖀𝚄𝕌',
		 'v𝐯𝑣𝒗𝗏𝘃𝘷𝙫𝓋𝓿𝔳𝖛𝚟𝕧V𝐕𝑉𝑽𝖵𝗩𝘝𝙑𝒱𝓥𝔙𝖁𝚅𝕍',
		 'w𝐰𝑤𝒘𝗐𝘄𝘸𝙬𝓌𝔀𝔴𝖜𝚠𝕨W𝐖𝑊𝑾𝖶𝗪𝘞𝙒𝒲𝓦𝔚𝖂𝚆𝕎',
		 'x𝐱𝑥𝒙𝗑𝘅𝘹𝙭𝓍𝔁𝔵𝖝𝚡𝕩X𝐗𝑋𝑿𝖷𝗫𝘟𝙓𝒳𝓧𝔛𝖃𝚇𝕏',
		 'y𝐲𝑦𝒚𝗒𝘆𝘺𝙮𝓎𝔂𝔶𝖞𝚢𝕪Y𝐘𝑌𝒀𝖸𝗬𝘠𝙔𝒴𝓨𝔜𝖄𝚈𝕐',
		 'z𝐳𝑧𝒛𝗓𝘇𝘻𝙯𝓏𝔃𝔷𝖟𝚣𝕫Z𝐙𝑍𝒁𝖹𝗭𝘡𝙕𝒵𝓩ℨ𝖅𝚉ℤ']

dic = {i:j for i, j in zip([chr(i) for i in range(97, 123)], letters)}

from pprint import pprint

pprint([eval("text.lower()%s"%("".join([f".replace(chr({j+97}), dic[chr({j+97})][{i}])" for j in range(26)]))) for i in range(28)])
