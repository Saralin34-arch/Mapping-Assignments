# Improved Legend Implementation for Web Maps
# This provides a movable, comprehensive legend that can house all legend items

def create_movable_legend(legend_items, title="Legend"):
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
        width: 280px;
        max-height: 400px;
        background-color: white;
        border: 2px solid #666;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        z-index: 1000;
        font-family: Arial, sans-serif;
        font-size: 12px;
        overflow-y: auto;
        cursor: move;
        opacity: 0.9;
        transition: opacity 0.3s;
    " onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.9'">
        
        <!-- Legend Header -->
        <div style="
            background-color: #2E8B57;
            color: white;
            padding: 8px 12px;
            font-weight: bold;
            font-size: 14px;
            border-radius: 6px 6px 0 0;
            cursor: move;
            display: flex;
            justify-content: space-between;
            align-items: center;
        ">
            <span>{title}</span>
            <span style="cursor: pointer; font-size: 16px;" onclick="toggleLegend()">−</span>
        </div>
        
        <!-- Legend Content -->
        <div id="legend-content" style="padding: 10px;">
    """
    
    # Add legend items
    for label, color, symbol in legend_items:
        legend_html += f"""
            <div style="
                display: flex;
                align-items: center;
                margin-bottom: 6px;
                padding: 2px 0;
            ">
                <span style="
                    color: {color};
                    font-size: 16px;
                    margin-right: 8px;
                    width: 20px;
                    text-align: center;
                ">{symbol}</span>
                <span style="
                    color: #333;
                    font-size: 11px;
                    line-height: 1.2;
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
    </script>
    """
    
    return legend_html

# Example usage for LEED projects map
def create_leed_legend():
    """Create legend for LEED projects map"""
    legend_items = [
        ("Platinum Certification", "#2E8B57", "●"),
        ("Gold Certification", "#FFD700", "●"),
        ("Silver Certification", "#C0C0C0", "●"),
        ("Certified", "#87CEEB", "●"),
        ("High-Rise Commercial", "#FF6B6B", "●"),
        ("Low-Rise Commercial", "#4ECDC4", "●"),
        ("Residential", "#45B7D1", "●"),
        ("Mixed Use", "#96CEB4", "●")
    ]
    
    return create_movable_legend(legend_items, "LEED Projects Legend")

# Example usage for energy consumption map
def create_energy_legend():
    """Create legend for energy consumption map"""
    legend_items = [
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
    
    return create_movable_legend(legend_items, "Energy Consumption Legend")

# Example usage for building types map
def create_building_types_legend():
    """Create legend for building types map"""
    legend_items = [
        ("Commercial (C1-C8)", "#FF6B6B", "■"),
        ("Residential (R1-R10)", "#4ECDC4", "■"),
        ("Manufacturing (M1-M3)", "#45B7D1", "■"),
        ("Special Districts", "#9B59B6", "■"),
        ("Parks & Open Space", "#95A5A6", "■"),
        ("Transportation", "#E67E22", "■"),
        ("Institutional", "#3498DB", "■"),
        ("Mixed Use", "#96CEB4", "■")
    ]
    
    return create_movable_legend(legend_items, "Building Types Legend")

# Function to add legend to a folium map
def add_legend_to_map(map_obj, legend_items, title="Legend"):
    """
    Add a movable legend to a folium map
    
    Parameters:
    map_obj: folium map object
    legend_items: list of tuples (label, color, symbol)
    title: legend title
    """
    legend_html = create_movable_legend(legend_items, title)
    map_obj.get_root().html.add_child(folium.Element(legend_html))

# Example of how to use in your notebook:
"""
# For LEED projects map:
leed_legend_items = [
    ("Platinum Certification", "#2E8B57", "●"),
    ("Gold Certification", "#FFD700", "●"),
    ("Silver Certification", "#C0C0C0", "●"),
    ("Certified", "#87CEEB", "●"),
    ("High-Rise Commercial", "#FF6B6B", "●"),
    ("Low-Rise Commercial", "#4ECDC4", "●"),
    ("Residential", "#45B7D1", "●"),
    ("Mixed Use", "#96CEB4", "●")
]

# Add legend to your map
add_legend_to_map(m, leed_legend_items, "LEED Projects Legend")

# Or use the predefined function:
legend_html = create_leed_legend()
m.get_root().html.add_child(folium.Element(legend_html))
""" 