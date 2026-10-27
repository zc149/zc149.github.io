from pathlib import Path
import re,html
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Image as PDFImage,HRFlowable,Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image
root=Path.cwd();W,H=A4;margin=40;width=W-80
pdfmetrics.registerFont(TTFont('M','C:/Windows/Fonts/malgun.ttf'));pdfmetrics.registerFont(TTFont('MB','C:/Windows/Fonts/malgunbd.ttf'));pdfmetrics.registerFontFamily('M',normal='M',bold='MB',italic='M',boldItalic='MB')
accent='#B7473B';ink='#333333';muted='#555555'
def st(name,size=9.7,leading=13.5,**kw):return ParagraphStyle(name,fontName='M',fontSize=size,leading=leading,wordWrap='CJK',textColor=colors.HexColor(ink),**kw)
styles={'p':st('body',spaceAfter=5),'li':st('bullet',leftIndent=9,firstLineIndent=-8,spaceAfter=3),'meta':st('metadata',8.5,11.7,spaceAfter=3)}
styles['meta'].textColor=colors.HexColor(muted)
for n,size,before in [(2,14,10),(3,11,9),(4,11,9),(5,9.5,6)]:
 styles[n]=st('h'+str(n),size,size*1.35,spaceBefore=before,spaceAfter=5,keepWithNext=True);styles[n].fontName='MB'
def inline(t):
 t=re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>',lambda m:'<link href="'+html.escape(m[1],quote=True)+'">'+html.escape(m[2])+'</link>',t)
 if '<link ' not in t:t=html.escape(t)
 t=re.sub(r'`([^`]+)`',r'\1',t)
 for term in ['약 5분','약 39% 단축','약 33% 절감','약 $300 → $200']:t=t.replace(term,'<b>'+term+'</b>')
 return t
s=re.sub(r'^---\n.*?\n---\n','',(root/'index.md').read_text(encoding='utf-8'),flags=re.S);s=re.sub(r'<div[^>]*></div>\n','',s)
a=s.index('#### EKS 신규');b=s.index('## 추가 운영 개선');c=s.index('## 오픈소스 기여');chunks=[s[:a],s[a:b],s[b:c],s[c:]]
story=[]
name=st('name',27,34,alignment=0);name.fontName='MB'
role=st('role',10,15,alignment=0);role.textColor=colors.HexColor(accent)
contact=st('contact',9,13.5,alignment=0)
class CirclePortrait(Flowable):
 def __init__(self,path,size=95):
  super().__init__();self.path=path;self.width=size;self.height=size
 def draw(self):
  c=self.canv;c.saveState();path=c.beginPath();path.circle(self.width/2,self.height/2,self.width/2);c.clipPath(path,stroke=0)
  with Image.open(self.path) as im:w,h=im.size
  scale=max(self.width/w,self.height/h);dw,dh=w*scale,h*scale
  c.drawImage(str(self.path),(self.width-dw)/2,(self.height-dh)/2,width=dw,height=dh,mask='auto');c.restoreState()
photo=CirclePortrait(root/'assets/img/profile.jpg')
header=Table([[photo,[Paragraph('김지관',name),Paragraph('DEVOPS ENGINEER',role),Paragraph('010-9895-5140  |  zc149@naver.com<br/><link href="https://github.com/zc149">github.com/zc149</link>',contact)]]],colWidths=[110,width-110]);header.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
for page,chunk in enumerate(chunks):
 if page:story.append(PageBreak())
 else:story.append(header)
 in_projects=False
 for line in chunk.splitlines():
  line=line.strip()
  if not line or line=='# DevOps Engineer':continue
  if line=='## 대표 경험':
   in_projects=True;story.append(Spacer(1,7))
  if in_projects and line=='### 씨제이올리브영주식회사':continue
  m=re.match(r'^(#{2,5}) (.*)',line)
  if m:
   level=len(m[1]);title=inline(m[2])
   if level==2:
    # A short colored opening followed by a fine horizontal rule, as in Awesome CV.
    title='<font color="'+accent+'">'+title[:2]+'</font>'+title[2:]
    story.append(Paragraph(title,styles[2]));rule=HRFlowable(width='100%',thickness=.55,color=colors.HexColor('#B8B8B8'),spaceAfter=6);rule.keepWithNext=True;story.append(rule)
   else:story.append(Paragraph(title,styles[level]))
  elif line.startswith('- '):
   t=line[2:];meta=bool(re.match(r'(기간|직무|역할|대상|기술|조직·관리 대상 규모):',t));story.append(Paragraph(('' if meta else '• ')+inline(t),styles['meta' if meta else 'li']))
  else:story.append(Paragraph(inline(line),styles['p']))
def footer(c,doc):
 c.setFillColor(colors.HexColor('#888888'));c.setFont('M',8);c.drawString(margin,23,'김지관 · DevOps Portfolio');c.drawRightString(W-margin,23,f'{doc.page} / 4')
out=root/'assets/docs/portfolio.pdf'
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=margin,rightMargin=margin,topMargin=29,bottomMargin=43,title='김지관 | DevOps Portfolio',author='김지관').build(story,onFirstPage=footer,onLaterPages=footer)
r=PdfReader(str(out));assert len(r.pages)==4,len(r.pages)
text='\n'.join(p.extract_text() for p in r.pages)
for line in s.splitlines():
 if not line.strip():continue
 plain=re.sub(r'<[^>]+>','',line);plain=re.sub(r'^#{1,5} |^- ','',plain).replace('`','')
 if plain=='DevOps Engineer':continue
 assert re.sub(r'\s','',plain) in re.sub(r'\s','',text),plain
assert len(r.pages[0].images)>0
pdf=pdfium.PdfDocument(str(out));contact=Image.new('RGB',(960,1380),'#e1e1e1')
for i,page in enumerate(pdf):
 im=page.render(scale=1.5).to_pil().convert('RGB');im.save(root/f'tmp/pdfs/page-{i+1}.png');im.thumbnail((480,680));contact.paste(im,((i%2)*480,(i//2)*690))
contact.save(root/'tmp/pdfs/review.png');print('4 pages; full source text and portrait verified')
