mid = ['41380', '36793', '1689', '25397', '857', '22199', '4744', '41433', '19429', '29223', '8676', '22147', '24531', '6547', '9989', '15039', '11111', '21995', '9919', '12967', '12581', '39195', '10396', '20787', '11285', '11633', '36456', '10719', '24913', '38186', '14345', '10163', '12293', '513', '28999', '14741', '34382', '2167', '1575', '32887', '32887', '37348', '12549', '16592', '12893', '35849', '15583', '34497', '1535', '28223', '38000', '9379', '16512', '37520', '223', '9330', '6746', '5630', '32901', '25537', '22297', '356', '9367', '28907', '25183', '14131', '37349', '39576', '27631', '33783', '17895', '8425', '37105', '17729', '10793', '15729', '38816', '8630', '11617', '8074', '20853', '10079', '10408', '12189', '9041', '11013', '41623', '9750', '14765', '35639', '28623', '7054', '41930', '16009', '1691', '6045', '36098', '32281', '2927', '17741', '7593', '28851', '11887', '38889', '8841', '18153', '7148', '31251', '93', '32792', '17247', '24455', '19769', '35062', '12445', '10213', '40496', '14833', '33487', '10397', '10110', '40729', '10620', '5081', '2926', '41168', '10589', '4437', '13667', '8246', '6325', '1735', '14293', '18897', '19815', '20507', '18095', '6512', '11933', '6324', '4155', '14199', '32729', '34136', '8769', '19369', '29803', '11179', '22535', '6201', '30296', '39587', '18039', '13599', '28497', '23277', '36885', '17777', '12531', '20047', '13759', '2476', '21033', '5940', '38329', '37450', '20973', '4063', '355', '16498', '79', '11577', '9253', '18277', '5681', '16524', '11757', '36475', '20021', '31765', '36470', '30911', '35790', '195', '37430', '22687', '23283', '2236', '20785', '19117', '21353', '22319', '7654', '16011', '14227', '18139', '41389', '4224', '25157', '2129', '36539', '34902', '39741', '33352', '38826', '21085', '35968', '14813', '28677', '8861', '35507', '23273', '28497', '1195', '14075']
# print(len(mid))

ja_title = ['１００万の命の上に俺は立っている', '３Ｄ彼女\u3000リアルガール', '秒速５センチメートル', 'アブソリュート・デュオ', 'エア・ギア', 'アカメが斬る！', 'あかね色に染まる坂', 'アクダマドライブ', '悪魔のリドル', 'アルドノア・ゼロ総集編', 'アマガミSS', '甘城ブリリアントパーク', '姉ログ 靄子姉さんの止まらないモノローグ', 'Angel Beats!（エンジェルビーツ）', 'あの日見た花の名前を僕達はまだ知らない', '劇場版 あの日見た花の名前を僕達はまだ知らない', 'アナザー', 'アオハライド', '青の祓魔師(エクソシスト)', 'アルカナ・ファミリア', '朝まで授業chu!', 'BEASTARS', 'ベン・トー', 'ブラック・ブレット［黒の銃弾］', 'ブラック★ロックシューター', 'ブラッドラッド', '僕のヒーローアカデミア', '僕は友達が少ない', '僕らはみんな河合荘 初めての', 'ぼくたちは勉強ができない', 'BTOOOM!', 'C - The Money of Soul & Possibility Ctrl.', 'カンピオーネ！', '天空の城ラピュタ', 'Charlotte（シャーロット）', '中二病でも恋がしたい！', 'シトラス', 'CLANNAD', 'コードギアス 反逆のルルーシュ', 'ダンジョンに出会いを求めるのは間違っているだろうか', 'ダンまち 外伝 ソード・オラトリア', '劇場版 ダンまち -オリオンの矢-', 'だから僕は、Hができない', 'ダンガンロンパ', '男子高校生の日常', 'ダーリン・イン・ザ・フランキス', 'デート・ア・ライブ', 'デスマーチからはじまる異世界狂想曲', 'デスノート', 'デス・パレード', '鬼滅の刃', '電波女と青春男', 'デビルサバイバー２ THE ANIMATION', 'どろろ', 'ドラゴンボール', 'ドラゴンクライシス!', 'デュラララ!!', '東のエデン', 'エロマンガ先生', "Fate/stay Night [Heaven's Feel]", 'Fate/stay Night [Unlimited Blade Works]', 'Fate/stay Night', 'フリージング', 'GATE（ゲート）自衛隊 彼の地にて、斯く戦えり', 'GANGSTA (ギャングスタ)', 'ガールズ&パンツァー', 'ゴブリンスレイヤー', "ゴブリンスレイヤー -GOBLIN'S CROWN-", 'GOD EATER', 'GODZILLA -怪獣惑星-', 'ゴールデンタイム', 'GOSICK -ゴシック-', 'ぐらんぶる', 'グリザイアの果実', 'ギルティクラウン', 'はぐれ勇者の鬼畜美学〈エステティカ〉恥じらいいっぱい', 'ハロー・ワールド', '緋弾のアリア', 'ハイスクールD×D', '学園黙示録 HIGHSCHOOL OF THE DEAD', '棺姫のチャイカ', '星空へ架かる橋', '蛍火の杜へ', '氷菓', 'IS〈インフィニット・ストラトス〉', '妖狐×僕SS', '異世界魔王と召喚少女の奴隷魔術', 'いつか天魔の黒ウサギ', 'イクシオン サーガ DT', 'Just Because!', '甲鉄城のカバネリ', '会長はメイド様!', '神様になった日', '神さまのいない日曜日', '風のスティグマ', '君に届け', '君の膵臓をたべたい', '君の名は', 'キミキス', '君のいる町', 'キスシス', '聲の形', 'ココロコネクト', 'この音とまれ！', 'これはゾンビですか?', '境界の彼方', 'れでぃ×ばと!', '機動戦士ガンダム 鉄血のオルフェンズ', '機動戦士ガンダムSEED', '機動戦士ガンダムUC（ユニコーン）RE:0096', '機巧少女〈マシンドール〉は傷つかない', '魔弾の王と戦姫 (ヴァナディース)', '魔法戦争', '魔法使いの嫁', '黄昏乙女×アムネジア', '真剣で私に恋しなさい！', '魔王学院の不適合者', 'まおゆう魔王勇者', '政宗くんのリベンジ', 'ましろ色シンフォニー', 'まよチキ!', 'メガロボクス', '未来日記', '〈物語〉シリーズ', 'マイセルフ; ユアセルフ', '泣きたい私は猫をかぶる', 'ナルト ブラッド・プリズン', 'ナルト 疾風伝 絆', 'ナルト 疾風伝 ROAD TO NINJA', 'ナルト 疾風伝 ザ・ロストタワー', 'ナルト 疾風伝 火の意志を継ぐ者', 'NARUTO -ナルト-', 'ねらわれた学園', 'ニセコイ', 'ノーゲーム・ノーライフ', 'ノラガミ', 'のうりん', 'にゃんこい！', '織田信奈の野望', 'おまもりひまり', 'ワンピース ストロングワールド', 'お兄ちゃんだけど愛さえあれば関係ないよねっ', 'Orange（オレンジ）', 'Orange －未来－', '俺の妹がこんなに可愛いわけがない', 'アウトブレイク・カンパニー', 'オーバーロード', 'パパのいうことを聞きなさい！', '寄生獣 セイの格率', 'プリンセスラバー!', '落第騎士の英雄譚《キャバルリィ》', 'Re：ゼロから始める異世界生活', 'れすきゅーME!', 'ロボティクス・ノーツ', '六花の勇者', '冴えない彼女〈ヒロイン〉の育てかた', '冴えない彼女〈ヒロイン〉の育てかた Fine', '最近、妹のようすがちょっとおかしいんだが', '坂道のアポロン', '桜Trick', 'さくら荘のペットな彼女', 'スクールデイズ', '星刻の竜騎士', '聖剣の刀鍛冶（ブラックスミス）', '青春ブタ野郎はゆめみる少女の夢を見ない', '青春ブタ野郎はバニーガール先輩の夢を見ない', '世界征服～謀略のズヴィズダー～', 'セキレイ', '灼眼のシャナ', '進撃の巨人', 'SHUFFLE! (シャッフル!)', '劇場版 シュタインズゲート 負荷領域のデジャヴ', 'STEINS;GATE', 'ストライク・ザ・ブラッド', 'サマーウォーズ', '翠星のガルガンティア', 'SAO -ソードアート・オンライン-', 'SAO オルタナティブ ガンゲイル・オンライン', 'SAO Extra Edition', '劇場版 SAO -オーディナル・スケール-', '多田くんは恋をしない', 'テイルズ オブ ゼスティリア ザ クロス', '盾の勇者の成り上がり', 'おねがい☆ティーチャー', '転生したらスライムだった件', 'TERRA FORMARS (テラフォーマーズ)', '残響のテロル', '時をかける少女', '魔法科高校の劣等生', 'とある飛空士への恋歌', '東京ESP', '東京喰種-トーキョーグール-', '東京マグニチュード8.0', '東京レイヴンズ', 'となりの怪物くん', 'となりの関くん', 'トニカクカワイイ', 'とらドラ！', 'トリニティセブン', 'True Tears', '月がきれい', '徒然チルドレン', 'VE 外伝 -永遠と自動手記人形-', 'ヴァイオレット・エヴァーガーデン', '天気の子', 'ウィッチクラフトワークス', 'ヲタクに恋は難しい', 'やはり俺の青春ラブコメはまちがっている', '山田くんと7人の魔女', 'ヨスガノソラ', 'ようこそ実力至上主義の教室へ', '四月は君の嘘', '勇者になれなかった俺はしぶしぶ就職を決意しました', 'ゼロの使い魔', '絶園のテンペスト']

# unsorted (read)
l1 = ['Boku Girl', 'Brawling Go', 'Close as Neighbor', 'Darling in the Franxx', 'Demon Slayer', 'Domestic Kanojo', 'Imawa no Kuni no Alice', 'In Bura!', 'Kagami no kuni no Harisugawa', 'Kanojo ni naru hi', 'Kimi no Iru Machi', 'Kishuku Gakkou no Juliet', 'Koe no Katachi', 'Naruto / Shippuden', 'Nozoki Ana', 'Prison School', 'ReLife', 'Real girl', 'Sakamichi no Apollon', 'The Breaker/ New wave', 'Tokyo Ghoul/ Re:', 'Unwated Roommate', 'Yamada-kun to 7-nin no Majo']

# unsorted (currently reading)
l2 = ['Btooom!', 'Kono Oto Tomare!', 'DICE', 'Kiss x Sis', 'Boruto: Next Generation', 'Shingeki no Kyojin', 'Solo Leveling', 'Supernova', 'Hige wo Soru', 'Black Clover', 'Kanojo Okarishimasu', 'Sensei wa koi wo Oshierarenai', 'Dosanko Gyaru is Mega Cute', 'Ponkotsu Fuukiin to Skaato take ga Futekisetsu na JK no Hanashi', 'Kakkou no Iinazuke', 'Yankee JK Kuzuhana-chan', 'Ijiranaide Nagatoror-san', 'Kaiko Sareta Ankoku Heishi', 'Neet Dakedo Hello Work ni Ittara Isekai ni Tsuretekareta', 'Kamigami ni Sodaterare Shimo No Saikyou to Naru']

# sorted both
l3 = ['Black Clover', 'Boku Girl', 'Boruto: Next Generation', 'Btooom!', 'Close as Neighbor','Darling in the Franxx', 'Demon Slayer', 'Domestic Kanojo', 'Dosanko Gyaru is Mega Cute', 'Hige wo Soru', 'Ijiranaide Nagatoror-san', 'Imawa no Kuni no Alice', 'In Bura!', 'Kagami no kuni no Harisugawa', 'Kaiko Sareta Ankoku Heishi', 'Kakkou no Iinazuke', 'Kamigami ni Sodaterare Shimo No Saikyou to Naru', 'Kanojo Okarishimasu', 'Kanojo ni naru hi', 'Kimi no Iru Machi', 'Kishuku Gakkou no Juliet', 'Kiss x Sis', 'Koe no Katachi', 'Kono Oto Tomare!', 'Naruto', 'Neet Dakedo Hello Work ni Ittara Isekai ni Tsuretekareta', 'Nozoki Ana', 'Ponkotsu Fuukiin to Skaato take ga Futekisetsu na JK no Hanashi', 'Prison School', 'ReLIFE', 'Real girl', 'Sakamichi no Apollon', 'Sensei wa koi wo Oshierarenai', 'Shingeki no Kyojin', 'Solo Leveling', 'The Breaker', 'Tokyo Ghoul', 'Yamada-kun to 7-nin no Majo', 'Yankee JK Kuzuhana-chan']

print(len(l3))

# sorted mal_id
l4 = ['86337', '63781', '95210', '1376', '20593', '96567', '934', '111512', '96792', '70941', '121597', '116201', '110737', '33031', '39839', '26584', '121485', '123602', '125206', '108407', '54817', '8483', '91514', '3048', '56805', '45143', '96765', '113558', '21419', '119260', '25297', '78523', '50767', '28393', '117080', '23390', '121496', '100145', '22651', '33327', '13233', '35003', '125345']

# sorted ja_title
l5 = ['ブラッククローバー', 'ボクガール', 'BORUTO-NARUTO NEXT GENERATIONS-', '狗-DOGS- Stray dogs howling in the dark', 'BTOOOM!', 'マイ・フェア・ネイバー', 'ダイス', 'ダーリン・イン・ザ・フランキス', '鬼滅の刃', 'ドメスティックな彼女', '道産子ギャルはなまらめんこい', 'ひげを剃る。そして女子高生を拾う。', 'イジらないで、長瀞さん', '今際の国のアリス', 'いんブラ！～美少女吸血鬼の恥ずかしい秘密～', '鏡の国の針栖川', '解雇された暗黒兵士（30代）のスローなセカンドライフ', 'カッコウの許嫁', '神々に育てられしもの、最強となる', '彼女、お借りします', '彼女になる日', '君のいる町', '寄宿学校のジュリエット', 'キス×シス', '聲の形', 'この音とまれ！', '劇場版NARUTO 疾風伝', 'ニートだけどハロワにいったら異世界につれてかれた', 'ノ・ゾ・キ・ア・ナ', 'ポンコツ風紀委員とスカート丈が不適切なJKの話', '監獄学園〈プリズンスクール〉', 'ReLIFE', '3D彼女〈リアルガール〉', '坂道のアポロン', '先生は恋を教えられない', '進撃の巨人', '나 혼자만 레벨업', 'ジェラテリアスーパーノヴァ', '브레이커NW', '東京喰種トーキョーグール', '毎日君に恋してる', '山田くんと7人の魔女', 'ヤンキーJKクズハナちゃん']

# sorted manga type
l6 = ['Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Light Novel', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Light Novel', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manga', 'Manhwa', 'Manga', 'Manhwa', 'Manga', 'Manga', 'Manga', 'Manga']