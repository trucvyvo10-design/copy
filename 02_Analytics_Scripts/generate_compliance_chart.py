import os
import numpy as np
import matplotlib.pyplot as plt

def generate_alert_precision_curve():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(base_dir, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    output_path = os.path.join(docs_dir, 'alert_precision_threshold_curve.png')

    thresholds = np.linspace(0.10, 0.90, 200)
    alert_volume = 5000 * np.exp(-3.2 * thresholds) + 400
    precision = 0.20 + 0.79 / (1 + np.exp(-11 * (thresholds - 0.42)))

    fig, ax1 = plt.subplots(figsize=(10, 5.5), dpi=300)

    color_red = '#c62828'
    ax1.set_xlabel('Decision Threshold (Risk Score Cutoff)', fontsize=12, labelpad=8)
    ax1.set_ylabel('Alert Volume', color=color_red, fontsize=12, labelpad=8)
    ax1.plot(thresholds, alert_volume, color=color_red, linewidth=2)
    ax1.tick_params(axis='y', labelcolor='black', labelsize=11)
    ax1.tick_params(axis='x', labelsize=11)
    ax1.set_ylim(200, 4700)
    ax1.set_xlim(0.08, 0.92)

    ax2 = ax1.twinx()
    color_blue = '#1565c0'
    ax2.set_ylabel('Precision Rate', color=color_blue, fontsize=12, labelpad=8)
    ax2.plot(thresholds, precision, color=color_blue, linewidth=2)
    ax2.tick_params(axis='y', labelcolor='black', labelsize=11)
    ax2.set_ylim(0.15, 1.05)

    plt.title('Compliance Operations: Alert Volume vs Precision Curve', fontsize=14, pad=12)
    fig.tight_layout()

    plt.savefig(output_path, dpi=300)
    print(f"✅ Successfully generated chart at: {output_path}")

if __name__ == '__main__':
    generate_alert_precision_curve()
