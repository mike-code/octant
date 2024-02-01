"""Insert budgets for epoch 2

Revision ID: 1d7b215a9201
Revises: 2de1bc96061a
Create Date: 2024-01-23 10:02:18.743673

"""
from alembic import op
from sqlalchemy.exc import SQLAlchemyError

from app.legacy.core.epochs.epoch_snapshots import has_pending_epoch_snapshot

# revision identifiers, used by Alembic.
revision = "1d7b215a9201"
down_revision = "2de1bc96061a"
branch_labels = None
depends_on = None


def upgrade():
    try:
        has_snapshot = has_pending_epoch_snapshot(2)
    except SQLAlchemyError:
        has_snapshot = False

    if has_snapshot:
        op.execute(sqltext())


def downgrade():
    op.execute("DELETE FROM budgets WHERE epoch = 2")


def sqltext():
    return """
INSERT INTO budgets (epoch, user_id, budget, created_at) VALUES
(2, 3426, '144998567921911', '2023-01-17'),
(2, 12691, '6367866205860722', '2023-01-17'),
(2, 10932, '96665711947940', '2023-01-17'),
(2, 12403, '966657119479408', '2023-01-17'),
(2, 10329, '106332283142734', '2023-01-17'),
(2, 79, '2555918775798117', '2023-01-17'),
(2, 7841, '117932168576487', '2023-01-17'),
(2, 12733, '1042718396597012307', '2023-01-17'),
(2, 2612, '214740675278449', '2023-01-17'),
(2, 12588, '253070833879709', '2023-01-17'),
(2, 216, '99407647450460', '2023-01-17'),
(2, 12641, '966657119479408', '2023-01-17'),
(2, 107, '966657119479408', '2023-01-17'),
(2, 52, '483328559739704', '2023-01-17'),
(2, 75, '579994271687645', '2023-01-17'),
(2, 13229, '130541416461215', '2023-01-17'),
(2, 13341, '2397521078618811', '2023-01-17'),
(2, 349, '97632369067420', '2023-01-17'),
(2, 1097, '96665711947940', '2023-01-17'),
(2, 777, '96665711947940', '2023-01-17'),
(2, 10389, '106332283142734', '2023-01-17'),
(2, 4664, '966657119479408', '2023-01-17'),
(2, 12694, '966657119479408', '2023-01-17'),
(2, 172, '966657119479408', '2023-01-17'),
(2, 12617, '966657119479408', '2023-01-17'),
(2, 5016, '966657119479408', '2023-01-17'),
(2, 10385, '106332283142734', '2023-01-17'),
(2, 10367, '106332283142734', '2023-01-17'),
(2, 12759, '4833285597397044', '2023-01-17'),
(2, 6670, '96665711947940', '2023-01-17'),
(2, 13301, '120724102672220', '2023-01-17'),
(2, 10384, '106332283142734', '2023-01-17'),
(2, 333, '96665711947940', '2023-01-17'),
(2, 6, '45824774820818076', '2023-01-17'),
(2, 2829, '966657119479408', '2023-01-17'),
(2, 13304, '144998567921911', '2023-01-17'),
(2, 2995, '241664279869852', '2023-01-17'),
(2, 13553, '725578583982864', '2023-01-17'),
(2, 4945, '96665711947940', '2023-01-17'),
(2, 965, '966657119479408', '2023-01-17'),
(2, 11500, '966657119479408', '2023-01-17'),
(2, 44, '869024750411988', '2023-01-17'),
(2, 12720, '386662847791763528', '2023-01-17'),
(2, 4529, '966657119479408', '2023-01-17'),
(2, 260, '966657119479408', '2023-01-17'),
(2, 60, '483328559739704', '2023-01-17'),
(2, 11543, '966657119479408', '2023-01-17'),
(2, 13352, '963948217050065', '2023-01-17'),
(2, 12463, '193331423895881', '2023-01-17'),
(2, 12732, '987232554596161835', '2023-01-17'),
(2, 13332, '920838468887310', '2023-01-17'),
(2, 185, '9986922909401491', '2023-01-17'),
(2, 12648, '966657119479408', '2023-01-17'),
(2, 12420, '472249723947834', '2023-01-17'),
(2, 13414, '18703027642407770', '2023-01-17'),
(2, 12817, '4833285597397044', '2023-01-17'),
(2, 6318, '966657119479408', '2023-01-17'),
(2, 53, '523623123279188', '2023-01-17'),
(2, 82, '966657119479408', '2023-01-17'),
(2, 7087, '966657119479408', '2023-01-17'),
(2, 108, '96665711947940', '2023-01-17'),
(2, 12418, '1159988543375290', '2023-01-17'),
(2, 10378, '106332283142734', '2023-01-17'),
(2, 12495, '966657119479408', '2023-01-17'),
(2, 2877, '966657119479408', '2023-01-17'),
(2, 7795, '483328559739704', '2023-01-17'),
(2, 10346, '106332283142734', '2023-01-17'),
(2, 13325, '966657119479408', '2023-01-17'),
(2, 1404, '130498711129720', '2023-01-17'),
(2, 13, '14499856792191132323', '2023-01-17'),
(2, 6686, '961823833882011', '2023-01-17'),
(2, 56, '966657119479408', '2023-01-17'),
(2, 16, '107298940262214', '2023-01-17'),
(2, 6687, '958923862523573', '2023-01-17'),
(2, 12832, '193331771423424', '2023-01-17'),
(2, 10337, '107298940262214', '2023-01-17'),
(2, 8220, '966657119479408', '2023-01-17'),
(2, 10481, '966657119479408', '2023-01-17'),
(2, 4680, '869991407531467', '2023-01-17'),
(2, 9986, '966657119479408', '2023-01-17'),
(2, 408, '841176795856924', '2023-01-17'),
(2, 13090, '966657119479408', '2023-01-17'),
(2, 12493, '106211451002800', '2023-01-17'),
(2, 1344, '97632369067420', '2023-01-17'),
(2, 12820, '101436164832571', '2023-01-17'),
(2, 9910, '97632369067420', '2023-01-17'),
(2, 6317, '966657119479408', '2023-01-17'),
(2, 12877, '97632369067420', '2023-01-17'),
(2, 18, '966657119479408', '2023-01-17'),
(2, 325, '966657119479408', '2023-01-17'),
(2, 13311, '172136429531204', '2023-01-17'),
(2, 12981, '966657119479408', '2023-01-17'),
(2, 13056, '966657119479408', '2023-01-17'),
(2, 1361, '966657119479408', '2023-01-17'),
(2, 12810, '966657119479408', '2023-01-17'),
(2, 130, '96665711947940882', '2023-01-17'),
(2, 13272, '17969189815567', '2023-01-17'),
(2, 13344, '462130062265162', '2023-01-17'),
(2, 11932, '966657119479408', '2023-01-17'),
(2, 1303, '117799736551119', '2023-01-17'),
(2, 12741, '1063311231541915950', '2023-01-17'),
(2, 277, '579994271687645', '2023-01-17'),
(2, 12649, '3363966775788342699', '2023-01-17'),
(2, 3802, '4833882012586756', '2023-01-17'),
(2, 255, '966657119479408', '2023-01-17'),
(2, 13479, '1869211103735173', '2023-01-17'),
(2, 12859, '101498997545337', '2023-01-17'),
(2, 13159, '1853451869569919', '2023-01-17'),
(2, 151, '966657119479408', '2023-01-17'),
(2, 13283, '98599026186899', '2023-01-17'),
(2, 10340, '106332283142734', '2023-01-17'),
(2, 51, '966657119479408', '2023-01-17'),
(2, 8172, '966657119479408', '2023-01-17'),
(2, 13088, '966657119479408', '2023-01-17'),
(2, 37, '241664279869852', '2023-01-17'),
(2, 13544, '2872557843496355', '2023-01-17'),
(2, 13275, '97632369067420', '2023-01-17'),
(2, 10394, '106332283142734', '2023-01-17'),
(2, 559, '966657119479408', '2023-01-17'),
(2, 10362, '106332283142734', '2023-01-17'),
(2, 13381, '1038998753631562', '2023-01-17'),
(2, 13637, '380680776440872', '2023-01-17'),
(2, 662, '433027931976495', '2023-01-17'),
(2, 206, '103103209783202', '2023-01-17'),
(2, 12771, '100550020279009', '2023-01-17'),
(2, 12875, '193331423895881', '2023-01-17'),
(2, 22, '966657119479408', '2023-01-17'),
(2, 10344, '106332283142734', '2023-01-17'),
(2, 7361, '966657119479408', '2023-01-17'),
(2, 6470, '956990548284614', '2023-01-17'),
(2, 219, '103080564678783', '2023-01-17'),
(2, 13562, '58154386621944', '2023-01-17'),
(2, 10393, '106332283142734', '2023-01-17'),
(2, 450, '104243981386272', '2023-01-17'),
(2, 207, '966657119479408', '2023-01-17'),
(2, 12854, '966657119479408', '2023-01-17'),
(2, 12474, '966657119479408', '2023-01-17'),
(2, 12517, '108265597381693', '2023-01-17'),
(2, 12783, '500349612336309', '2023-01-17'),
(2, 4936, '96665711947940', '2023-01-17'),
(2, 264, '966657119479408', '2023-01-17'),
(2, 84, '966657119479408', '2023-01-17'),
(2, 4952, '96665711947940', '2023-01-17'),
(2, 12998, '144998567921911', '2023-01-17'),
(2, 10341, '106332283142734', '2023-01-17'),
(2, 6895, '965690462359929', '2023-01-17'),
(2, 142, '100532340425858', '2023-01-17'),
(2, 12662, '97632369067420', '2023-01-17'),
(2, 1269, '96665711947940', '2023-01-17'),
(2, 4867, '966657119479408', '2023-01-17'),
(2, 134, '966657119479408', '2023-01-17'),
(2, 57, '966657119479408', '2023-01-17'),
(2, 12731, '1735007628679714350', '2023-01-17'),
(2, 148, '8945629319577255', '2023-01-17'),
(2, 13500, '1836694675350506', '2023-01-17'),
(2, 155, '104398968903776', '2023-01-17'),
(2, 13501, '1090845917219461', '2023-01-17'),
(2, 10168, '97632369067420', '2023-01-17'),
(2, 10380, '106332283142734', '2023-01-17'),
(2, 8280, '966657119479408', '2023-01-17'),
(2, 254, '966657119479408', '2023-01-17'),
(2, 4641, '966657119479408', '2023-01-17'),
(2, 40, '966657119479408', '2023-01-17'),
(2, 12999, '483328559739704', '2023-01-17'),
(2, 13499, '4268384986726578', '2023-01-17'),
(2, 12828, '98600460023688', '2023-01-17'),
(2, 13460, '2118972159271364', '2023-01-17'),
(2, 49, '966657119479408', '2023-01-17'),
(2, 149, '1583749712221472', '2023-01-17'),
(2, 12555, '97226884098731032', '2023-01-17'),
(2, 212, '103911716123487', '2023-01-17'),
(2, 221, '99226809931864', '2023-01-17'),
(2, 12622, '2475736576798105', '2023-01-17'),
(2, 461, '96665711947940', '2023-01-17'),
(2, 547, '966657119479408', '2023-01-17'),
(2, 137, '107298940262214', '2023-01-17'),
(2, 12744, '777205857261127070', '2023-01-17'),
(2, 218, '99930698866687', '2023-01-17'),
(2, 13548, '5945955782590740', '2023-01-17'),
(2, 150, '966657119479408', '2023-01-17'),
(2, 20, '966657119479408', '2023-01-17'),
(2, 5250, '96665711947940', '2023-01-17'),
(2, 103, '966657119479408', '2023-01-17'),
(2, 5204, '106332283142734', '2023-01-17'),
(2, 8211, '1933314238958817', '2023-01-17'),
(2, 164, '34750407117467857', '2023-01-17'),
(2, 141, '101498997545337', '2023-01-17'),
(2, 200, '100219274152073', '2023-01-17'),
(2, 13550, '273846298621440610', '2023-01-17'),
(2, 272, '483328559739704', '2023-01-17'),
(2, 12475, '96665711947940', '2023-01-17'),
(2, 154, '966657119479408', '2023-01-17'),
(2, 24, '483328559739704', '2023-01-17'),
(2, 58, '351740589906233907', '2023-01-17'),
(2, 12616, '966657119479408', '2023-01-17'),
(2, 12757, '1329265793833941', '2023-01-17'),
(2, 13123, '203825910214440', '2023-01-17'),
(2, 13066, '96018153614468', '2023-01-17'),
(2, 68, '966657119479408', '2023-01-17'),
(2, 7962, '483328559739704', '2023-01-17'),
(2, 152, '1449985679219113', '2023-01-17'),
(2, 235, '966657119479408', '2023-01-17'),
(2, 12807, '906641115820424', '2023-01-17'),
(2, 10387, '106332283142734', '2023-01-17'),
(2, 12891, '2024584676884417', '2023-01-17'),
(2, 10360, '106332283142734', '2023-01-17'),
(2, 5257, '470762017186472', '2023-01-17'),
(2, 13076, '966657119479408', '2023-01-17'),
(2, 13353, '943083478917380', '2023-01-17'),
(2, 8608, '1546651391167054', '2023-01-17'),
(2, 13152, '966657119479408', '2023-01-17'),
(2, 10159, '97632369067420', '2023-01-17'),
(2, 203, '106354057939238', '2023-01-17'),
(2, 27, '193331423895881', '2023-01-17'),
(2, 10089, '966657119479408', '2023-01-17'),
(2, 13374, '99697828541884', '2023-01-17'),
(2, 12948, '966657119479408', '2023-01-17'),
(2, 10368, '106332283142734', '2023-01-17'),
(2, 13630, '11713483428842219', '2023-01-17'),
(2, 12808, '2583981243785107', '2023-01-17'),
(2, 13401, '49665417502918366', '2023-01-17'),
(2, 475, '483328559739704', '2023-01-17'),
(2, 12929, '387760556738926', '2023-01-17'),
(2, 1031, '966657119479408', '2023-01-17'),
(2, 10354, '106332283142734', '2023-01-17'),
(2, 13564, '62989601349773', '2023-01-17'),
(2, 12852, '193331423895881', '2023-01-17'),
(2, 7807, '193331423895881', '2023-01-17'),
(2, 3169, '241664279869852', '2023-01-17'),
(2, 10359, '106332283142734', '2023-01-17'),
(2, 13233, '72499283960955661', '2023-01-17'),
(2, 12742, '386651247906329775', '2023-01-17'),
(2, 62, '966657119479408', '2023-01-17'),
(2, 13268, '101315922603403', '2023-01-17'),
(2, 12661, '185160364312832', '2023-01-17'),
(2, 6341, '966657119479408', '2023-01-17'),
(2, 6333, '966657119479408', '2023-01-17'),
(2, 13194, '768630176107073', '2023-01-17'),
(2, 9501, '96665711947940', '2023-01-17'),
(2, 1948, '96665711947940', '2023-01-17'),
(2, 7334, '108369918913638', '2023-01-17'),
(2, 220, '98716362809851', '2023-01-17'),
(2, 4043, '966657119479408', '2023-01-17'),
(2, 8984, '1004440267772869', '2023-01-17'),
(2, 4480, '97632369067420', '2023-01-17'),
(2, 8329, '376401558294187', '2023-01-17'),
(2, 10357, '106332283142734', '2023-01-17'),
(2, 10104, '966657119479408', '2023-01-17'),
(2, 3909, '207212864170262', '2023-01-17'),
(2, 12152, '966657119479408', '2023-01-17'),
(2, 7747, '96762377659888', '2023-01-17'),
(2, 209, '121933401123761095', '2023-01-17'),
(2, 10167, '97632369067420', '2023-01-17'),
(2, 443, '96665711947940', '2023-01-17'),
(2, 10391, '106332283142734', '2023-01-17'),
(2, 2056, '3520727638417992', '2023-01-17'),
(2, 10383, '106332283142734', '2023-01-17'),
(2, 222, '100764582955492', '2023-01-17'),
(2, 54, '966657119479408', '2023-01-17'),
(2, 13274, '99565683306379', '2023-01-17'),
(2, 13008, '121334801637055', '2023-01-17'),
(2, 10330, '106332283142734', '2023-01-17'),
(2, 13284, '265136790896928', '2023-01-17'),
(2, 9689, '966657119479408', '2023-01-17'),
(2, 1015, '105365626023255', '2023-01-17'),
(2, 13281, '483328559739704', '2023-01-17'),
(2, 13073, '103442128464940', '2023-01-17'),
(2, 246, '966657119479408', '2023-01-17'),
(2, 3755, '966657119479408', '2023-01-17'),
(2, 4898, '966657119479408', '2023-01-17'),
(2, 10370, '106332283142734', '2023-01-17'),
(2, 204, '105541025687862', '2023-01-17'),
(2, 245, '483328559739704', '2023-01-17'),
(2, 77, '77332569558352705', '2023-01-17'),
(2, 205, '104728020334020', '2023-01-17'),
(2, 1584, '96665711947940', '2023-01-17'),
(2, 261, '966657119479408', '2023-01-17'),
(2, 13072, '966657119479408', '2023-01-17'),
(2, 119, '966657119479408', '2023-01-17'),
(2, 12554, '966657119479408', '2023-01-17'),
(2, 8193, '1027374924573340', '2023-01-17'),
(2, 12470, '966657119479408', '2023-01-17'),
(2, 4440, '89293935044156942', '2023-01-17'),
(2, 12827, '96665711947940882', '2023-01-17'),
(2, 85, '129242056874396', '2023-01-17'),
(2, 12931, '966657119479408', '2023-01-17'),
(2, 366, '418422077455123', '2023-01-17'),
(2, 12848, '144998567921911323', '2023-01-17'),
(2, 10343, '106332283142734', '2023-01-17'),
(2, 5175, '144998567921911323', '2023-01-17'),
(2, 13616, '82525574496424812', '2023-01-17'),
(2, 4384, '483328559739704', '2023-01-17'),
(2, 8926, '3863295440967173', '2023-01-17'),
(2, 10381, '106332283142734', '2023-01-17'),
(2, 174, '966657119479408', '2023-01-17'),
(2, 8878, '967623776598888', '2023-01-17'),
(2, 12857, '111040273573276', '2023-01-17'),
(2, 11509, '966657119479408', '2023-01-17'),
(2, 816, '966657119479408', '2023-01-17'),
(2, 12781, '99773100041225', '2023-01-17'),
(2, 36, '442180357682952', '2023-01-17'),
(2, 10331, '106332283142734', '2023-01-17'),
(2, 4591, '108724179519174', '2023-01-17'),
(2, 6896, '956990548284614', '2023-01-17'),
(2, 10347, '106332283142734', '2023-01-17'),
(2, 225, '966657119479408', '2023-01-17'),
(2, 9993, '966657119479408', '2023-01-17'),
(2, 7133, '483328559739704', '2023-01-17'),
(2, 110, '99780636354000', '2023-01-17'),
(2, 12333, '237614871830253', '2023-01-17'),
(2, 4550, '142195262275421', '2023-01-17'),
(2, 3959, '140165282324514', '2023-01-17'),
(2, 208, '102290275037082', '2023-01-17'),
(2, 12863, '48332855973970441', '2023-01-17'),
(2, 9980, '966657119479408', '2023-01-17'),
(2, 4996, '97632369067420', '2023-01-17'),
(2, 390, '115998854337529', '2023-01-17'),
(2, 12815, '62178125466509021', '2023-01-17'),
(2, 10327, '106332283142734', '2023-01-17'),
(2, 10395, '106332283142734', '2023-01-17'),
(2, 2, '966657119479408', '2023-01-17'),
(2, 10426, '966657119479408', '2023-01-17'),
(2, 13273, '100484222176944', '2023-01-17'),
(2, 12805, '145808626588035', '2023-01-17'),
(2, 10353, '106332283142734', '2023-01-17'),
(2, 171, '9666571194794088', '2023-01-17'),
(2, 109, '9520955466611713', '2023-01-17'),
(2, 13702, '105213142311278309', '2023-01-17'),
(2, 10334, '106332283142734', '2023-01-17'),
(2, 12489, '966657119479408', '2023-01-17'),
(2, 6332, '966657119479408', '2023-01-17'),
(2, 1438, '133438514967419', '2023-01-17'),
(2, 165, '483328559739704410', '2023-01-17'),
(2, 8951, '966657119479408', '2023-01-17'),
(2, 12491, '117802324949554', '2023-01-17'),
(2, 112, '948521980518372', '2023-01-17'),
(2, 6348, '966657119479408', '2023-01-17'),
(2, 12728, '146562927048201282', '2023-01-17'),
(2, 10332, '106332283142734', '2023-01-17'),
(2, 10397, '106332283142734', '2023-01-17'),
(2, 5338, '578576870055958', '2023-01-17'),
(2, 12452, '109976580483172', '2023-01-17'),
(2, 2092, '1246221874679796', '2023-01-17'),
(2, 10386, '106332283142734', '2023-01-17'),
(2, 10325, '106332283142734', '2023-01-17'),
(2, 7088, '3122302495918490', '2023-01-17'),
(2, 11643, '1446013298452324', '2023-01-17'),
(2, 10358, '106332283142734', '2023-01-17'),
(2, 4722, '966657119479408', '2023-01-17'),
(2, 12816, '89162613700478034', '2023-01-17'),
(2, 13074, '97729034779368', '2023-01-17'),
(2, 11741, '966657119479408', '2023-01-17'),
(2, 467, '966657119479408', '2023-01-17'),
(2, 12762, '96666678605060351898', '2023-01-17'),
(2, 9647, '483328559739704', '2023-01-17'),
(2, 12844, '96665711947940', '2023-01-17'),
(2, 996, '108144765241758', '2023-01-17'),
(2, 59, '966657119479408', '2023-01-17'),
(2, 138, '98599026186899', '2023-01-17'),
(2, 12419, '966657119479408', '2023-01-17'),
(2, 7505, '966657119479408', '2023-01-17'),
(2, 50, '966657119479408', '2023-01-17'),
(2, 7538, '966657119479408', '2023-01-17'),
(2, 9589, '96665711947940', '2023-01-17'),
(2, 7072, '956990548284614', '2023-01-17'),
(2, 10342, '106332283142734', '2023-01-17'),
(2, 1933, '966657119479408', '2023-01-17'),
(2, 159, '6253939416424262', '2023-01-17'),
(2, 11606, '966657119479408', '2023-01-17'),
(2, 332, '289997135843822', '2023-01-17'),
(2, 13458, '2112684754109677', '2023-01-17'),
(2, 153, '483328559739704', '2023-01-17'),
(2, 13556, '1082793348178088', '2023-01-17'),
(2, 90, '966657119479408', '2023-01-17'),
(2, 13004, '122591455892378', '2023-01-17'),
(2, 38, '966657119479408', '2023-01-17'),
(2, 1659, '5752183596341688', '2023-01-17'),
(2, 10355, '106332283142734', '2023-01-17'),
(2, 13345, '96452701791790', '2023-01-17'),
(2, 194, '966657119479408', '2023-01-17'),
(2, 269, '241664279869852', '2023-01-17'),
(2, 293, '966657119479408', '2023-01-17'),
(2, 11194, '505429821456633', '2023-01-17'),
(2, 10356, '106332283142734', '2023-01-17'),
(2, 12934, '1098122487728608', '2023-01-17'),
(2, 12400, '966657119479408', '2023-01-17'),
(2, 9372, '966657119479408', '2023-01-17'),
(2, 6349, '966657119479408', '2023-01-17'),
(2, 160, '296559406028075', '2023-01-17'),
(2, 189, '966657119479408', '2023-01-17'),
(2, 7181, '966657119479408', '2023-01-17'),
(2, 6688, '959890519643052', '2023-01-17'),
(2, 6362, '966657119479408', '2023-01-17'),
(2, 12525, '1196624848203560', '2023-01-17'),
(2, 4647, '966657119479408', '2023-01-17'),
(2, 3929, '966657119479408', '2023-01-17'),
(2, 13611, '74941894351777', '2023-01-17'),
(2, 162, '217812634773571409', '2023-01-17'),
(2, 10372, '106332283142734', '2023-01-17'),
(2, 10339, '106332283142734', '2023-01-17'),
(2, 3213, '193331423895881', '2023-01-17'),
(2, 5201, '96665711947940', '2023-01-17'),
(2, 12716, '989297323375897', '2023-01-17'),
(2, 12775, '104398968903776', '2023-01-17'),
(2, 5031, '106332283142734', '2023-01-17'),
(2, 253, '966657119479408', '2023-01-17'),
(2, 12681, '931495762844113', '2023-01-17'),
(2, 7071, '966657119479408', '2023-01-17'),
(2, 1202, '318996849428204', '2023-01-17'),
(2, 12624, '966657119479408', '2023-01-17'),
(2, 6678, '961823833882011', '2023-01-17'),
(2, 3080, '97632369067420', '2023-01-17'),
(2, 13558, '581339065303864', '2023-01-17'),
(2, 4983, '106332283142734', '2023-01-17'),
(2, 12921, '966657119479408', '2023-01-17'),
(2, 769, '99565683306379', '2023-01-17'),
(2, 10365, '106332283142734', '2023-01-17'),
(2, 12774, '100532340425858', '2023-01-17'),
(2, 1187, '105848954582995', '2023-01-17'),
(2, 2879, '106178584660737', '2023-01-17'),
(2, 12502, '966657119479408', '2023-01-17'),
(2, 13330, '643793641573286', '2023-01-17'),
(2, 1546, '96665711947940', '2023-01-17'),
(2, 13320, '270601243529857', '2023-01-17'),
(2, 1223, '96665711947940', '2023-01-17'),
(2, 12739, '834321759822677753', '2023-01-17'),
(2, 8134, '16433171031149949', '2023-01-17'),
(2, 12636, '483328559739704', '2023-01-17'),
(2, 10382, '106332283142734', '2023-01-17'),
(2, 13051, '966657119479408', '2023-01-17'),
(2, 10366, '106332283142734', '2023-01-17'),
(2, 10398, '106332283142734', '2023-01-17'),
(2, 3161, '966657119479408', '2023-01-17'),
(2, 12118, '966657119479408', '2023-01-17'),
(2, 10479, '407135968747236', '2023-01-17'),
(2, 434, '104882297463515', '2023-01-17'),
(2, 6340, '966657119479408', '2023-01-17'),
(2, 26, '966657119479408', '2023-01-17'),
(2, 167, '966657119479408', '2023-01-17'),
(2, 12650, '2609007565474924', '2023-01-17'),
(2, 10369, '106332283142734', '2023-01-17'),
(2, 12629, '39381431377879396', '2023-01-17'),
(2, 13438, '447471311431762', '2023-01-17'),
(2, 66, '1933314238958817', '2023-01-17'),
(2, 10336, '106332283142734', '2023-01-17'),
(2, 97, '966657119479408', '2023-01-17'),
(2, 3279, '162156324056160', '2023-01-17'),
(2, 12761, '1914918151958769973', '2023-01-17'),
(2, 156, '966657119479408', '2023-01-17'),
(2, 8020, '241664279869852', '2023-01-17'),
(2, 13447, '219395018794100', '2023-01-17'),
(2, 10, '100229310944395', '2023-01-17'),
(2, 12436, '126520917083062', '2023-01-17'),
(2, 9553, '193331423895881', '2023-01-17'),
(2, 10392, '106332283142734', '2023-01-17'),
(2, 10471, '966657119479408', '2023-01-17'),
(2, 10328, '106332283142734', '2023-01-17'),
(2, 2040, '96665711947940', '2023-01-17'),
(2, 12743, '805080381958425637', '2023-01-17'),
(2, 14, '3384087314476223142', '2023-01-17'),
(2, 10338, '106332283142734', '2023-01-17'),
(2, 4570, '193331423895881', '2023-01-17'),
(2, 12007, '966657119479408', '2023-01-17'),
(2, 143, '101498997545337', '2023-01-17'),
(2, 12888, '966657119479408', '2023-01-17'),
(2, 91, '1163493657161689', '2023-01-17'),
(2, 12770, '966657119479408', '2023-01-17'),
(2, 12394, '3673297054021753521', '2023-01-17'),
(2, 12942, '8332063100328617', '2023-01-17'),
(2, 157, '483328559739704', '2023-01-17'),
(2, 94, '966657119479408', '2023-01-17'),
(2, 4792, '869991407531467', '2023-01-17'),
(2, 217, '99429799230552', '2023-01-17'),
(2, 12839, '338329991817793087', '2023-01-17'),
(2, 2192, '96665711947940', '2023-01-17'),
(2, 182, '966657119479408', '2023-01-17'),
(2, 5239, '96665711947940', '2023-01-17'),
(2, 12927, '1890589077681296', '2023-01-17'),
(2, 12638, '338329991817793087', '2023-01-17'),
(2, 12826, '549055606706646', '2023-01-17'),
(2, 13318, '243036932979512', '2023-01-17'),
(2, 4972, '106332283142734', '2023-01-17'),
(2, 12997, '483328559739704', '2023-01-17'),
(2, 6273, '918324263505438', '2023-01-17'),
(2, 13296, '966657119479408', '2023-01-17'),
(2, 1424, '101498997545337', '2023-01-17'),
(2, 12738, '2416642798698522', '2023-01-17'),
(2, 48, '966657119479408', '2023-01-17'),
(2, 13060, '966657119479408', '2023-01-17'),
(2, 10363, '106332283142734', '2023-01-17'),
(2, 1234, '966657119479408', '2023-01-17'),
(2, 8841, '966657119479408', '2023-01-17'),
(2, 13410, '262681111220338', '2023-01-17'),
(2, 10361, '106332283142734', '2023-01-17'),
(2, 13638, '39054034180098', '2023-01-17'),
(2, 12391, '14238645670087565', '2023-01-17'),
(2, 13321, '966657119479408', '2023-01-17'),
(2, 10379, '106332283142734', '2023-01-17'),
(2, 11956, '966657119479408', '2023-01-17'),
(2, 4930, '97632369067420', '2023-01-17'),
(2, 70, '966657119479408', '2023-01-17'),
(2, 11519, '470762017186472', '2023-01-17'),
(2, 177, '97632369067420', '2023-01-17'),
(2, 13298, '487671118072233', '2023-01-17'),
(2, 81, '4630728941252818', '2023-01-17'),
(2, 9638, '966657119479408', '2023-01-17'),
(2, 140, '101498997545337', '2023-01-17'),
(2, 12675, '138231968085555', '2023-01-17'),
(2, 25, '966657119479408', '2023-01-17'),
(2, 4557, '966657119479408', '2023-01-17'),
(2, 13346, '100063107402891', '2023-01-17'),
(2, 233, '661821761426652', '2023-01-17'),
(2, 6967, '97632369067420', '2023-01-17'),
(2, 12913, '755925867432897698', '2023-01-17'),
(2, 13206, '966657119479408', '2023-01-17'),
(2, 12734, '966648539795304055', '2023-01-17'),
(2, 10364, '106332283142734', '2023-01-17'),
(2, 763, '966657119479408', '2023-01-17'),
(2, 13340, '1875400881046837', '2023-01-17'),
(2, 31, '496633151518898', '2023-01-17'),
(2, 6893, '956990548284614', '2023-01-17'),
(2, 178, '1063322831427349', '2023-01-17'),
(2, 7823, '193331423895881', '2023-01-17'),
(2, 13303, '145578562193598', '2023-01-17'),
(2, 122, '966657119479408', '2023-01-17'),
(2, 12088, '1181418465347705', '2023-01-17'),
(2, 12965, '748246538084670', '2023-01-17'),
(2, 12729, '966657119479408', '2023-01-17'),
(2, 10396, '106332283142734', '2023-01-17'),
(2, 13282, '96889645699427', '2023-01-17'),
(2, 12, '966657119479408', '2023-01-17'),
(2, 12953, '819367340476077', '2023-01-17'),
(2, 11677, '966657119479408', '2023-01-17'),
(2, 183, '327412783112092', '2023-01-17'),
(2, 2503, '483328559739704', '2023-01-17'),
(2, 13624, '146034883638519', '2023-01-17'),
(2, 144, '97632369067420', '2023-01-17'),
(2, 12866, '96665711947940', '2023-01-17'),
(2, 10335, '106332283142734', '2023-01-17'),
(2, 133, '106332283142734', '2023-01-17'),
(2, 13557, '472391655644174', '2023-01-17'),
(2, 4636, '242377672824028', '2023-01-17'),
(2, 13650, '92241051508859', '2023-01-17'),
(2, 215, '101731394204024', '2023-01-17'),
(2, 1565, '106332283142734', '2023-01-17'),
(2, 13280, '104147659577662', '2023-01-17'),
(2, 11955, '966657119479408', '2023-01-17'),
(2, 13351, '185262101201873', '2023-01-17'),
(2, 12747, '867189133954063758', '2023-01-17'),
(2, 201, '103299844473078', '2023-01-17'),
(2, 12873, '98619609232578', '2023-01-17'),
(2, 30, '1106476531886573', '2023-01-17'),
(2, 658, '98599026186899', '2023-01-17'),
(2, 12985, '966657119479408', '2023-01-17'),
(2, 13649, '25743751320017', '2023-01-17'),
(2, 1183, '966657119479408', '2023-01-17'),
(2, 12795, '966657119479408', '2023-01-17'),
(2, 13091, '966657119479408', '2023-01-17'),
(2, 8237, '1550053522148312', '2023-01-17'),
(2, 10345, '106332283142734', '2023-01-17'),
(2, 8327, '3652668591092062', '2023-01-17'),
(2, 12377, '966657119479408', '2023-01-17'),
(2, 13559, '749359228677650', '2023-01-17'),
(2, 72, '966657119479408', '2023-01-17'),
(2, 282, '966657119479408', '2023-01-17'),
(2, 12803, '966657119479408', '2023-01-17'),
(2, 4519, '97632369067420', '2023-01-17'),
(2, 10333, '106332283142734', '2023-01-17'),
(2, 9856, '971296316340022', '2023-01-17'),
(2, 11942, '1136857468595307', '2023-01-17'),
(2, 10390, '106332283142734', '2023-01-17'),
(2, 11696, '966657119479408', '2023-01-17'),
(2, 5048, '98599026186899', '2023-01-17'),
(2, 210, '100665551700268', '2023-01-17'),
(2, 11875, '966657119479408', '2023-01-17'),
(2, 226, '966657119479408', '2023-01-17'),
(2, 10371, '106332283142734', '2023-01-17'),
(2, 243, '966657119479408', '2023-01-17'),
(2, 39, '966657119479408', '2023-01-17'),
(2, 13309, '146323178172733', '2023-01-17'),
(2, 13554, '727077849434464', '2023-01-17'),
(2, 12503, '966657119479408', '2023-01-17'),
(2, 13549, '228637293385400', '2023-01-17'),
(2, 13620, '185047025692719', '2023-01-17'),
(2, 13067, '152297175980884', '2023-01-17'),
(2, 273, '966657119479408', '2023-01-17')
"""