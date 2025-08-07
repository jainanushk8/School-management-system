import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import os

warnings.filterwarnings("ignore")

def create_single_window_dashboard():
    """Create all ML visualizations in one clean window"""
    
    # Configure matplotlib to prevent multiple windows
    plt.ioff()  # Turn off interactive mode to prevent multiple windows
    
    # Create the main figure with proper spacing
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('ML Options Comprehensive Dashboard', fontsize=20, fontweight='bold', y=0.95)
    
    # Define the data
    models = ['Attend Pred', 'HW Delay', 'Stud Risk', 'Lesson Perf']
    implementation = [1, 0, 1, 0]  # 1=implemented, 0=not implemented
    business_impact = [3, 2, 5, 3]
    complexity = [3, 3, 2, 4]
    accuracy = [85, 70, 100, 75]
    
    # Create DataFrame for easier handling
    df = pd.DataFrame({
        'Model': models,
        'Implementation': implementation,
        'Business': business_impact,
        'Complexity': complexity,
        'Accuracy': accuracy
    })
    
    # Calculate priority scores
    priority_scores = df['Implementation'] * df['Business'] * (6 - df['Complexity'])
    
    # Create 2x2 subplots with proper spacing
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Subplot 1: Bar chart (top-left)
    ax1 = fig.add_subplot(gs[0, 0])
    x = np.arange(len(models))
    width = 0.25
    
    bars1 = ax1.bar(x - width, implementation, width, label='Implementation', color='#2E8B57', alpha=0.8)
    bars2 = ax1.bar(x, business_impact, width, label='Business Impact', color='#20B2AA', alpha=0.8)
    bars3 = ax1.bar(x + width, complexity, width, label='Complexity', color='#DAA520', alpha=0.8)
    
    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'{int(height)}', 
                        xy=(bar.get_x() + bar.get_width()/2, height),
                        xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom', fontweight='bold')
    
    ax1.set_title('ML Option Comp Scores', fontweight='bold', fontsize=14)
    ax1.set_xlabel('ML Options', fontweight='bold')
    ax1.set_ylabel('Score', fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(models, rotation=0)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.set_ylim(0, 6)
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Scatter plot (top-right)
    ax2 = fig.add_subplot(gs[0, 1])
    colors = ['green' if impl else 'red' for impl in implementation]
    sizes = [300 if impl else 150 for impl in implementation]
    
    scatter = ax2.scatter(complexity, accuracy, c=colors, s=sizes, alpha=0.7, edgecolors='black', linewidth=2)
    
    for i, model in enumerate(models):
        ax2.annotate(model, (complexity[i], accuracy[i]), 
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=9, fontweight='bold')
    
    ax2.set_xlabel('Complexity (1-5)', fontweight='bold')
    ax2.set_ylabel('Expected Accuracy (%)', fontweight='bold')
    ax2.set_title('Complexity vs Accuracy Analysis', fontweight='bold', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 5)
    ax2.set_ylim(60, 105)
    
    # Add legend
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='green', 
                             markersize=10, label='Implemented'),
                      Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
                             markersize=10, label='Not Implemented')]
    ax2.legend(handles=legend_elements, loc='lower right', fontsize=10)
    
    # Subplot 3: Priority Heatmap (bottom-left)
    ax3 = fig.add_subplot(gs[1, 0])
    
    # Create heatmap data
    heatmap_data = np.array([priority_scores.values])
    im = ax3.imshow(heatmap_data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=max(priority_scores))
    
    ax3.set_xticks(range(len(models)))
    ax3.set_xticklabels(models, rotation=45, ha='right')
    ax3.set_yticks([0])
    ax3.set_yticklabels(['Priority Score'])
    ax3.set_title('Implementation Priority Heatmap', fontweight='bold', fontsize=14)
    
    # Add text annotations
    for i, score in enumerate(priority_scores):
        ax3.text(i, 0, f'{int(score)}', ha='center', va='center', 
                color='black', fontweight='bold', fontsize=12)
    
    # Subplot 4: Business Impact by Status (bottom-right)
    ax4 = fig.add_subplot(gs[1, 1])
    
    # Group data by implementation status
    implemented_impact = [business_impact[i] for i in range(len(models)) if implementation[i]]
    not_implemented_impact = [business_impact[i] for i in range(len(models)) if not implementation[i]]
    
    avg_implemented = np.mean(implemented_impact) if implemented_impact else 0
    avg_not_implemented = np.mean(not_implemented_impact) if not_implemented_impact else 0
    
    categories = ['Not Implemented', 'Implemented']
    values = [avg_not_implemented, avg_implemented]
    colors_bar = ['red', 'green']
    
    bars = ax4.bar(categories, values, color=colors_bar, alpha=0.7, width=0.6)
    
    ax4.set_ylabel('Average Business Impact', fontweight='bold')
    ax4.set_title('Business Impact by Implementation Status', fontweight='bold', fontsize=14)
    ax4.set_ylim(0, 6)
    ax4.grid(True, alpha=0.3)
    
    # Add value labels
    for bar, value in zip(bars, values):
        ax4.annotate(f'{value:.1f}', 
                    xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontweight='bold')
    
    # Save and show in single window
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig('ml_dashboard_complete.png', dpi=300, bbox_inches='tight')
    plt.show()  # This will show all plots in ONE window
    
    # Create summary table
    create_summary_table(df, priority_scores)

def create_summary_table(df, priority_scores):
    """Create and display summary table"""
    
    # Add priority scores to dataframe
    df['Priority_Score'] = priority_scores
    df['Status'] = ['✓ Implemented' if impl else '✗ Not Implemented' for impl in df['Implementation']]
    
    print("\n" + "="*80)
    print("ML OPTIONS COMPREHENSIVE ANALYSIS")
    print("="*80)
    
    # Display formatted table
    for i, row in df.iterrows():
        print(f"\n{i+1}. {row['Model']}")
        print(f"   Status: {row['Status']}")
        print(f"   Business Impact: {row['Business']}/5")
        print(f"   Complexity: {row['Complexity']}/5")
        print(f"   Expected Accuracy: {row['Accuracy']}%")
        print(f"   Priority Score: {int(row['Priority_Score'])}")
        print("-" * 40)
    
    # Save to Excel
    df.to_excel('ml_dashboard_analysis.xlsx', index=False)
    print(f"\nAnalysis saved to: ml_dashboard_analysis.xlsx")
    print("Dashboard image saved to: ml_dashboard_complete.png")
    print("="*80)

def main():
    """Main function to run the dashboard"""
    print("Creating ML Options Dashboard...")
    print("All visualizations will appear in ONE window")
    print("-" * 50)
    
    create_single_window_dashboard()
    
    print("\n✅ Dashboard created successfully!")
    print("📊 All 4 charts displayed in single window")
    print("📁 Files generated:")
    print("   - ml_dashboard_complete.png")
    print("   - ml_dashboard_analysis.xlsx")

if __name__ == "__main__":
    main()
