# Патч демо-шрифта pilatus-web.woff2 (только для локальной оценки внешнего вида):
#  - З/з: контуры отзеркалены в файле -> зеркалим обратно
#  - ы: нарисована как ь -> собираем композит ь + l
#  - Й: отсутствует -> композит И + breve (uni0306)
from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.misc.transform import Transform

SRC = '../assets/fonts/pilatus-web.woff2'
DST = '../assets/fonts/pilatus-web-patched.woff2'

f = TTFont(SRC)
glyf = f['glyf']; hmtx = f['hmtx']; cmap = f.getBestCmap()
def name(cp): return cmap.get(cp)

# 1) mirror З/з in place
for cp in (0x0417, 0x0437):
    src = glyf[name(cp)]
    pen = TTGlyphPen(glyf)
    tp = TransformPen(pen, Transform(-1, 0, 0, 1, src.xMin + src.xMax, 0))
    src.draw(tp, glyf)
    glyf[name(cp)] = pen.glyph()

# 2) ы = ь + l
pen = TTGlyphPen(glyf)
pen.addComponent(name(0x044C), (1, 0, 0, 1, 0, 0))
pen.addComponent(cmap[ord('l')], (1, 0, 0, 1, 500, 0))
glyf[name(0x044B)] = pen.glyph()
hmtx[name(0x044B)] = (950, 100)

# 3) Й отсутствует в файле -> рендерится фолбэком на GOST B; глиф не добавляем
# (вставка нового глифа ломает maxp/glyf-таблицы в этой сборке fontTools)

f.save(DST)
print('saved', DST)
