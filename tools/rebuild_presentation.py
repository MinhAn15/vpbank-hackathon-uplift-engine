"""
Rebuild presentation PDF from docs assets (uses matplotlib)
Run from repository root: python tools/rebuild_presentation.py
"""
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
docs = os.path.join(workspace, 'docs')

roi_csv = os.path.join(docs, 'roi.csv')
qini_png = os.path.join(docs, 'qini_curve.png')
arch_png = os.path.join(docs, 'architecture.png')
roi_bar = os.path.join(docs, 'roi_bar.png')
presentation_pdf = os.path.join(docs, 'presentation.pdf')

if not os.path.exists(roi_csv):
    raise FileNotFoundError(roi_csv)

roi = pd.read_csv(roi_csv)

# regenerate ROI bar
roi_plot = roi.set_index('strategy')
order = ['traditional', 'uplift_top30pct_model']
vals_ordered = [float(roi_plot.loc[o,'roi_pct']) for o in order]
labels = ['Before', 'After']
colors = ['#d62728', '#2ca02c']
plt.figure(figsize=(8,5))
bars = plt.bar(labels, vals_ordered, color=colors)
for bar, v in zip(bars, vals_ordered):
    plt.text(bar.get_x() + bar.get_width()/2, v + 0.5, f"{v:.1f}%", ha='center', va='bottom')
plt.ylabel('ROI (%)')
plt.title('Marketing ROI: Before vs After')
plt.tight_layout()
plt.savefig(roi_bar)
plt.close()

# build presentation
mantra = "Giải pháp Uplift Engine nâng ROI từ 19.2% lên 78.3% — tăng thêm 59.1 điểm phần trăm, tiết kiệm 70% ngân sách."
with PdfPages(presentation_pdf) as pdf:
    # title
    fig = plt.figure(figsize=(11,8.5))
    plt.axis('off')
    plt.text(0.5,0.6,'Uplift Engine — Demo & Impact', ha='center', fontsize=36)
    pdf.savefig(fig); plt.close(fig)

    # other slides simplified...
    fig = plt.figure(figsize=(11,8.5)); plt.axis('off'); plt.text(0.1,0.5,mantra); pdf.savefig(fig); plt.close(fig)
    fig = plt.figure(figsize=(11,8.5)); plt.axis('off')
    if os.path.exists(arch_png):
        img = plt.imread(arch_png); plt.imshow(img); plt.axis('off')
    else:
        plt.text(0.1,0.5,'Architecture missing')
    pdf.savefig(fig); plt.close(fig)

    fig = plt.figure(figsize=(11,8.5)); plt.axis('off')
    if os.path.exists(qini_png):
        img = plt.imread(qini_png); plt.imshow(img); plt.axis('off')
    pdf.savefig(fig); plt.close(fig)

    fig = plt.figure(figsize=(11,8.5)); plt.axis('off')
    if os.path.exists(roi_bar):
        img = plt.imread(roi_bar); plt.imshow(img); plt.axis('off')
    pdf.savefig(fig); plt.close(fig)

print('Rebuilt presentation at', presentation_pdf)
