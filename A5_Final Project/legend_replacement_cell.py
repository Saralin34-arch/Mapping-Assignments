# CELL: Improved Movable Legend Implementation
# Add this cell to your notebook to replace existing legend implementations

def create_improved_legend(legend_items, title="Legend"):
    """
    Create a movable legend with all legend items
    
    Parameters:
    legend_items: list of tuples (label, color, symbol)
    title: legend title
    
    Returns:
    HTML string for the legend
    """
    
    legend_html = f"""
    <div id="legend" style="
        position: absolute;
        top: 10px;
        right: 10px;
        width: 300px;
        max-height: 450px;
        background-color: white;
        border: 2px solid #666;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 1000;
        font-family: Arial, sans-serif;
        font-size: 12px;
        overflow-y: auto;
        cursor: move;
        opacity: 0.95;
        transition: opacity 0.3s;
    " onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.95'">
        
        <!-- Legend Header -->
        <div style="
            background: linear-gradient(135deg, #2E8B57, #3CB371);
            color: white;
            padding: 10px 15px;
            font-weight: bold;
            font-size: 14px;
            border-radius: 6px 6px 0 0;
            cursor: move;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        ">
            <span>🗺️ {title}</span>
            <span style="cursor: pointer; font-size: 18px; font-weight: bold;" onclick="toggleLegend()">−</span>
        </div>
        
        <!-- Legend Content -->
        <div id="legend-content" style="padding: 12px;">
    """
    
    # Add legend items
    for label, color, symbol in legend_items:
        legend_html += f"""
            <div style="
                display: flex;
                align-items: center;
                margin-bottom: 8px;
                padding: 3px 0;
                border-bottom: 1px solid #f0f0f0;
            ">
                <span style="
                    color: {color};
                    font-size: 18px;
                    margin-right: 10px;
                    width: 25px;
                    text-align: center;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
                ">{symbol}</span>
                <span style="
                    color: #333;
                    font-size: 11px;
                    line-height: 1.3;
                    font-weight: 500;
                ">{label}</span>
            </div>
        """
    
    legend_html += """
        </div>
    </div>
    
    <!-- JavaScript for movable legend -->
    <script>
        // Make legend draggable
        function makeDraggable(element) {
            let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
            
            element.onmousedown = dragMouseDown;
            
            function dragMouseDown(e) {
                e = e || window.event;
                e.preventDefault();
                // get the mouse cursor position at startup
                pos3 = e.clientX;
                pos4 = e.clientY;
                document.onmouseup = closeDragElement;
                document.onmousemove = elementDrag;
            }
            
            function elementDrag(e) {
                e = e || window.event;
                e.preventDefault();
                // calculate the new cursor position
                pos1 = pos3 - e.clientX;
                pos2 = pos4 - e.clientY;
                pos3 = e.clientX;
                pos4 = e.clientY;
                // set the element's new position
                element.style.top = (element.offsetTop - pos2) + "px";
                element.style.left = (element.offsetLeft - pos1) + "px";
                element.style.right = "auto";
                element.style.bottom = "auto";
            }
            
            function closeDragElement() {
                document.onmouseup = null;
                document.onmousemove = null;
            }
        }
        
        // Toggle legend visibility
        function toggleLegend() {
            const content = document.getElementById('legend-content');
            const toggleBtn = document.querySelector('#legend span:last-child');
            
            if (content.style.display === 'none') {
                content.style.display = 'block';
                toggleBtn.textContent = '−';
            } else {
                content.style.display = 'none';
                toggleBtn.textContent = '+';
            }
        }
        
        // Initialize draggable functionality
        window.onload = function() {
            const legend = document.getElementById('legend');
            if (legend) {
                makeDraggable(legend);
            }
        };
        
        // Add keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            if (e.key === 'h' || e.key === 'H') {
                const legend = document.getElementById('legend');
                if (legend) {
                    legend.style.display = legend.style.display === 'none' ? 'block' : 'none';
                }
            }
        });
    </script>
    """
    
    return legend_html

# Predefined legend configurations for your maps
def get_leed_legend_items():
    """Get legend items for LEED projects map"""
    return [
        ("Platinum Certification", "#2E8B57", "●"),
        ("Gold Certification", "#FFD700", "●"),
        ("Silver Certification", "#C0C0C0", "●"),
        ("Certified", "#87CEEB", "●"),
        ("High-Rise Commercial", "#FF6B6B", "●"),
        ("Low-Rise Commercial", "#4ECDC4", "●"),
        ("Residential", "#45B7D1", "●"),
        ("Mixed Use", "#96CEB4", "●"),
        ("Office Buildings", "#DDA0DD", "●"),
        ("Retail/Commercial", "#F0E68C", "●")
    ]

def get_energy_legend_items():
    """Get legend items for energy consumption map"""
    return [
        ("Very Low Energy Use", "#2E8B57", "●"),
        ("Low Energy Use", "#90EE90", "●"),
        ("Medium Energy Use", "#FFFF00", "●"),
        ("High Energy Use", "#FFA500", "●"),
        ("Very High Energy Use", "#FF0000", "●"),
        ("Commercial Buildings", "#4682B4", "●"),
        ("Residential Buildings", "#32CD32", "●"),
        ("Mixed Use Buildings", "#9370DB", "●"),
        ("Office Buildings", "#20B2AA", "●"),
        ("Retail Buildings", "#FF69B4", "●")
    ]

def get_building_types_legend_items():
    """Get legend items for building types map"""
    return [
        ("Commercial (C1-C8)", "#FF6B6B", "■"),
        ("Residential (R1-R10)", "#4ECDC4", "■"),
        ("Manufacturing (M1-M3)", "#45B7D1", "■"),
        ("Special Districts", "#9B59B6", "■"),
        ("Parks & Open Space", "#95A5A6", "■"),
        ("Transportation", "#E67E22", "■"),
        ("Institutional", "#3498DB", "■"),
        ("Mixed Use", "#96CEB4", "■")
    ]

# Function to add legend to a folium map
def add_improved_legend_to_map(map_obj, legend_items, title="Legend"):
    """
    Add a movable legend to a folium map
    
    Parameters:
    map_obj: folium map object
    legend_items: list of tuples (label, color, symbol)
    title: legend title
    """
    legend_html = create_improved_legend(legend_items, title)
    map_obj.get_root().html.add_child(folium.Element(legend_html))

# Example usage for your existing maps:
"""
# For LEED projects map:
leed_items = get_leed_legend_items()
add_improved_legend_to_map(m, leed_items, "LEED Projects Legend")

# For energy consumption map:
energy_items = get_energy_legend_items()
add_improved_legend_to_map(m, energy_items, "Energy Consumption Legend")

# For building types map:
building_items = get_building_types_legend_items()
add_improved_legend_to_map(m, building_items, "Building Types Legend")

# Or create custom legend items:
custom_items = [
    ("Your Category 1", "#FF0000", "●"),
    ("Your Category 2", "#00FF00", "●"),
    ("Your Category 3", "#0000FF", "●"),
]
add_improved_legend_to_map(m, custom_items, "Custom Legend")
""" 