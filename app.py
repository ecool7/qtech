from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page='home')

@app.route('/about')
def about():
    return render_template('about.html', page='about')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', page='contacts')

@app.route('/developments')
def developments():
    return render_template('developments.html', page='developments')

@app.route('/technologies')
def technologies():
    return render_template('technologies.html', page='technologies')

@app.route('/news')
def news():
    # Список актуальных новостей (3 последних разработки с главной страницы)
    news_articles = [
        {
            'id': 1,
            'title': 'Autonomous Delivery Robot Revolution',
            'description': 'Advanced autonomous delivery robot for smart city logistics and last-mile delivery solutions.',
            'image': 'robot.jpg',
            'category': 'Technology',
            'date': '2024-12-15',
            'content': 'A breakthrough in last‑mile logistics: AI navigation, obstacle avoidance and secure contactless delivery.',
            'tags': ['Autonomous', 'Delivery', 'AI', 'Smart City']
        },
        {
            'id': 2,
            'title': 'Smart Charger Station Innovation',
            'description': 'Intelligent EV charging with smart‑grid integration and renewable energy optimization.',
            'image': 'charge.jpg',
            'category': 'Industrial',
            'date': '2024-11-20',
            'content': 'Ultra‑fast charging up to 350 kW, V2G support and AI‑driven load management for lower costs.',
            'tags': ['EV Charging', 'Smart Grid', 'Renewables', 'IoT']
        },
        {
            'id': 4,
            'title': 'Smart Home Automation Revolution',
            'description': 'Integrated smart‑home system with IoT sensors, energy management and voice control.',
            'image': 'cleverdom.jpg',
            'category': 'Smart Home',
            'date': '2024-09-05',
            'content': 'Comprehensive automation platform: safety, comfort and energy savings powered by AI and Matter.',
            'tags': ['Smart Home', 'IoT', 'Automation', 'Energy']
        }
    ]
    return render_template('news.html', page='news', articles=news_articles)

@app.route('/news/<int:article_id>')
def news_article(article_id):
    # Получаем все новости
    news_articles = [
        {
            'id': 1,
            'title': 'Autonomous Delivery Robot Revolution',
            'description': 'Advanced autonomous delivery robot for smart city logistics and last-mile delivery solutions',
            'image': 'robot.jpg',
            'category': 'Technology',
            'date': '2024-12-15',
            'content': 'Quxiang Technology introduces a revolutionary autonomous delivery robot designed for smart city logistics and last-mile delivery solutions. This cutting-edge robot combines advanced AI navigation, obstacle avoidance, and secure package delivery capabilities.',
            'tags': ['Autonomous', 'Delivery', 'AI', 'Smart City', 'Logistics'],
            'full_content': '''
            <h3>Revolutionary Delivery Technology</h3>
            <p>Our autonomous delivery robot represents a breakthrough in last-mile delivery solutions, designed to transform urban logistics and reduce delivery costs while improving efficiency and environmental sustainability.</p>
            
            <h3>Advanced Navigation System</h3>
            <p>The robot features state-of-the-art navigation capabilities:</p>
            <ul>
                <li><strong>LiDAR Technology:</strong> 360-degree obstacle detection and mapping</li>
                <li><strong>Computer Vision:</strong> Advanced image recognition for path planning</li>
                <li><strong>GPS Integration:</strong> Precise location tracking and route optimization</li>
                <li><strong>Machine Learning:</strong> Adaptive behavior based on environmental conditions</li>
                <li><strong>Real-time Processing:</strong> Instant decision-making for safe navigation</li>
            </ul>
            
            <h3>Smart City Integration</h3>
            <p>Designed specifically for smart city environments:</p>
            <ul>
                <li><strong>Traffic Management:</strong> Integration with smart traffic systems</li>
                <li><strong>Weather Adaptation:</strong> Operation in various weather conditions</li>
                <li><strong>Pedestrian Safety:</strong> Advanced collision avoidance systems</li>
                <li><strong>Infrastructure Compatibility:</strong> Works with existing urban infrastructure</li>
                <li><strong>Scalable Fleet Management:</strong> Centralized control of multiple robots</li>
            </ul>
            
            <h3>Delivery Capabilities</h3>
            <p>The robot offers comprehensive delivery solutions:</p>
            <ul>
                <li><strong>Secure Compartments:</strong> Weatherproof and tamper-resistant storage</li>
                <li><strong>Temperature Control:</strong> Climate-controlled delivery for sensitive items</li>
                <li><strong>Multi-package Support:</strong> Simultaneous delivery of multiple orders</li>
                <li><strong>Contactless Delivery:</strong> Safe, touch-free package handover</li>
                <li><strong>Real-time Tracking:</strong> Live delivery status updates for customers</li>
            </ul>
            
            <h3>Environmental Benefits</h3>
            <p>Our delivery robot contributes to sustainable urban development:</p>
            <ul>
                <li><strong>Zero Emissions:</strong> Electric-powered operation</li>
                <li><strong>Reduced Traffic:</strong> Decreased delivery vehicle congestion</li>
                <li><strong>Energy Efficiency:</strong> Optimized power consumption</li>
                <li><strong>Noise Reduction:</strong> Quiet operation in residential areas</li>
                <li><strong>Carbon Footprint:</strong> Significant reduction in delivery emissions</li>
            </ul>
            
            <h3>Future Applications</h3>
            <p>The autonomous delivery robot is designed for various applications:</p>
            <ul>
                <li>E-commerce last-mile delivery</li>
                <li>Food and grocery delivery services</li>
                <li>Pharmaceutical and medical supply delivery</li>
                <li>Corporate document and package delivery</li>
                <li>Emergency supply distribution</li>
            </ul>
            '''
        },
        {
            'id': 2,
            'title': 'Smart Charger Station Innovation',
            'description': 'Intelligent EV charging station with smart grid integration and renewable energy optimization',
            'image': 'charge.jpg',
            'category': 'Industrial',
            'date': '2024-11-20',
            'content': 'Quxiang Technology unveils a revolutionary smart charger station that integrates seamlessly with smart grid infrastructure and optimizes renewable energy usage for electric vehicle charging.',
            'tags': ['EV Charging', 'Smart Grid', 'Renewable Energy', 'IoT', 'Sustainability'],
            'full_content': '''
            <h3>Next-Generation EV Charging</h3>
            <p>Our smart charger station represents a quantum leap in electric vehicle charging technology, combining intelligent power management, renewable energy integration, and advanced grid connectivity to create the most efficient charging solution available.</p>
            
            <h3>Smart Grid Integration</h3>
            <p>The charger station features advanced smart grid capabilities:</p>
            <ul>
                <li><strong>Bidirectional Power Flow:</strong> Vehicle-to-grid (V2G) energy transfer</li>
                <li><strong>Dynamic Load Management:</strong> Real-time grid demand response</li>
                <li><strong>Peak Shaving:</strong> Intelligent power distribution during high demand</li>
                <li><strong>Grid Stabilization:</strong> Frequency regulation and voltage support</li>
                <li><strong>Predictive Analytics:</strong> AI-powered grid optimization</li>
            </ul>
            
            <h3>Renewable Energy Optimization</h3>
            <p>Advanced renewable energy integration features:</p>
            <ul>
                <li><strong>Solar Integration:</strong> Direct connection to solar panel arrays</li>
                <li><strong>Wind Power Support:</strong> Compatibility with wind energy systems</li>
                <li><strong>Energy Storage:</strong> Built-in battery storage for renewable energy</li>
                <li><strong>Smart Scheduling:</strong> Charging optimization based on renewable availability</li>
                <li><strong>Carbon Footprint Tracking:</strong> Real-time environmental impact monitoring</li>
            </ul>
            
            <h3>Advanced Charging Technology</h3>
            <p>State-of-the-art charging capabilities:</p>
            <ul>
                <li><strong>Ultra-Fast Charging:</strong> Up to 350 kW DC fast charging</li>
                <li><strong>Multi-Standard Support:</strong> CCS, CHAdeMO, and Tesla compatibility</li>
                <li><strong>Dynamic Power Allocation:</strong> Intelligent power sharing between vehicles</li>
                <li><strong>Thermal Management:</strong> Advanced cooling systems for optimal performance</li>
                <li><strong>Safety Systems:</strong> Comprehensive protection and monitoring</li>
            </ul>
            
            <h3>IoT and Connectivity</h3>
            <p>Comprehensive connectivity and monitoring:</p>
            <ul>
                <li><strong>5G Connectivity:</strong> Ultra-low latency communication</li>
                <li><strong>Cloud Integration:</strong> Remote monitoring and management</li>
                <li><strong>Mobile App:</strong> User-friendly charging control and payment</li>
                <li><strong>Predictive Maintenance:</strong> AI-powered system health monitoring</li>
                <li><strong>Real-time Analytics:</strong> Performance optimization and reporting</li>
            </ul>
            
            <h3>Environmental Impact</h3>
            <p>Our smart charger station contributes to environmental sustainability:</p>
            <ul>
                <li><strong>Carbon Reduction:</strong> Significant decrease in transportation emissions</li>
                <li><strong>Renewable Integration:</strong> Maximized use of clean energy sources</li>
                <li><strong>Energy Efficiency:</strong> Optimized power conversion and distribution</li>
                <li><strong>Waste Reduction:</strong> Minimal environmental footprint</li>
                <li><strong>Sustainable Materials:</strong> Eco-friendly construction and components</li>
            </ul>
            
            <h3>Commercial Applications</h3>
            <p>The smart charger station is designed for various commercial environments:</p>
            <ul>
                <li>Public charging networks and highway rest stops</li>
                <li>Corporate campuses and office buildings</li>
                <li>Shopping centers and retail locations</li>
                <li>Fleet charging depots and logistics centers</li>
                <li>Residential communities and apartment complexes</li>
            </ul>
            '''
        },
        {
            'id': 3,
            'title': 'SparkFun MGM240P Thing Plus',
            'description': 'Wireless IoT development platform with Matter support',
            'image': 'mgm240p.jpg',
            'category': 'IoT',
            'date': '2024-10-10',
            'content': 'The MGM240P Thing Plus is a powerful wireless development board featuring the MGM240P module with Matter support, enabling seamless integration with smart home ecosystems.',
            'tags': ['IoT', 'Wireless', 'Matter', 'Smart Home'],
            'full_content': '''
            <h3>Smart Home Revolution</h3>
            <p>The SparkFun MGM240P Thing Plus represents the next generation of IoT development boards, specifically designed for smart home applications with native Matter protocol support.</p>
            
            <h3>Matter Protocol Integration</h3>
            <p>Matter is the new standard for smart home connectivity, ensuring interoperability between devices from different manufacturers. The MGM240P Thing Plus provides:</p>
            <ul>
                <li>Native Matter protocol support</li>
                <li>Thread and Wi-Fi connectivity</li>
                <li>Secure device commissioning</li>
                <li>Cross-platform compatibility</li>
            </ul>
            
            <h3>Hardware Features</h3>
            <ul>
                <li><strong>Processor:</strong> ARM Cortex-M33 with TrustZone security</li>
                <li><strong>Wireless:</strong> Dual-band Wi-Fi 6 and Thread support</li>
                <li><strong>Memory:</strong> 1.5 MB Flash, 256 KB RAM</li>
                <li><strong>I/O:</strong> Multiple GPIO pins with ADC capabilities</li>
                <li><strong>Power:</strong> USB-C power and battery support</li>
            </ul>
            
            <h3>Development Ecosystem</h3>
            <p>SparkFun provides extensive documentation, tutorials, and community support for developers working with the MGM240P Thing Plus platform.</p>
            '''
        },
        {
            'id': 4,
            'title': 'Smart Home Automation Revolution',
            'description': 'Integrated smart home automation system with IoT sensors, energy management, and voice control',
            'image': 'cleverdom.jpg',
            'category': 'Smart Home',
            'date': '2024-09-05',
            'content': 'Quxiang Technology introduces a comprehensive smart home automation system that seamlessly integrates IoT sensors, advanced energy management, and intuitive voice control to create the ultimate connected living experience.',
            'tags': ['Smart Home', 'IoT', 'Automation', 'Energy Management', 'Voice Control'],
            'full_content': '''
            <h3>Revolutionary Home Automation</h3>
            <p>Our integrated smart home system represents the pinnacle of residential automation technology, combining cutting-edge IoT sensors, intelligent energy management, and seamless voice control to transform any home into a truly smart living environment.</p>
            
            <h3>Comprehensive IoT Integration</h3>
            <p>The system features extensive IoT sensor network:</p>
            <ul>
                <li><strong>Environmental Sensors:</strong> Temperature, humidity, air quality monitoring</li>
                <li><strong>Motion Detection:</strong> Advanced occupancy sensing and security</li>
                <li><strong>Light Sensors:</strong> Automatic lighting control and optimization</li>
                <li><strong>Door/Window Sensors:</strong> Comprehensive security and automation triggers</li>
                <li><strong>Water Leak Detection:</strong> Early warning system for water damage prevention</li>
                <li><strong>Smoke/CO Detection:</strong> Enhanced safety and emergency response</li>
            </ul>
            
            <h3>Intelligent Energy Management</h3>
            <p>Advanced energy optimization capabilities:</p>
            <ul>
                <li><strong>Smart Thermostats:</strong> AI-powered climate control and scheduling</li>
                <li><strong>Energy Monitoring:</strong> Real-time consumption tracking and analysis</li>
                <li><strong>Peak Demand Management:</strong> Automatic load balancing and optimization</li>
                <li><strong>Renewable Integration:</strong> Solar panel and battery storage management</li>
                <li><strong>Cost Optimization:</strong> Time-of-use pricing and energy savings</li>
                <li><strong>Predictive Analytics:</strong> Machine learning for energy efficiency</li>
            </ul>
            
            <h3>Voice Control and AI Assistant</h3>
            <p>Natural language interaction and AI-powered automation:</p>
            <ul>
                <li><strong>Multi-Platform Support:</strong> Amazon Alexa, Google Assistant, Apple Siri</li>
                <li><strong>Natural Language Processing:</strong> Conversational command recognition</li>
                <li><strong>Context Awareness:</strong> Intelligent understanding of user intent</li>
                <li><strong>Routine Automation:</strong> Customizable daily and weekly schedules</li>
                <li><strong>Learning Capabilities:</strong> Adaptive behavior based on user preferences</li>
                <li><strong>Multi-Room Audio:</strong> Synchronized music and announcements</li>
            </ul>
            
            <h3>Security and Privacy</h3>
            <p>Enterprise-grade security and privacy protection:</p>
            <ul>
                <li><strong>End-to-End Encryption:</strong> Secure data transmission and storage</li>
                <li><strong>Local Processing:</strong> Privacy-preserving edge computing</li>
                <li><strong>Access Control:</strong> Multi-factor authentication and user management</li>
                <li><strong>Data Protection:</strong> GDPR-compliant data handling</li>
                <li><strong>Secure Updates:</strong> Encrypted firmware and software updates</li>
                <li><strong>Intrusion Detection:</strong> Advanced security monitoring and alerts</li>
            </ul>
            
            <h3>Smart Lighting and Climate</h3>
            <p>Intelligent environmental control systems:</p>
            <ul>
                <li><strong>Adaptive Lighting:</strong> Circadian rhythm optimization and mood lighting</li>
                <li><strong>Zone Control:</strong> Individual room temperature and lighting management</li>
                <li><strong>Weather Integration:</strong> Automatic adjustment based on outdoor conditions</li>
                <li><strong>Occupancy Sensing:</strong> Smart on/off and dimming based on presence</li>
                <li><strong>Energy Efficiency:</strong> LED optimization and power management</li>
                <li><strong>Scene Control:</strong> Customizable lighting and climate scenes</li>
            </ul>
            
            <h3>Mobile App and Remote Access</h3>
            <p>Comprehensive mobile control and monitoring:</p>
            <ul>
                <li><strong>Intuitive Interface:</strong> User-friendly mobile application</li>
                <li><strong>Remote Monitoring:</strong> Real-time home status and alerts</li>
                <li><strong>Geofencing:</strong> Location-based automation triggers</li>
                <li><strong>Guest Access:</strong> Temporary access control for visitors</li>
                <li><strong>Energy Reports:</strong> Detailed consumption and savings analytics</li>
                <li><strong>Maintenance Alerts:</strong> Proactive system health monitoring</li>
            </ul>
            
            <h3>Integration and Compatibility</h3>
            <p>Seamless integration with existing and future technologies:</p>
            <ul>
                <li><strong>Matter Protocol:</strong> Universal smart home device compatibility</li>
                <li><strong>Zigbee/Z-Wave:</strong> Support for legacy smart home devices</li>
                <li><strong>Wi-Fi 6:</strong> High-speed wireless connectivity</li>
                <li><strong>Thread Network:</strong> Mesh networking for reliable communication</li>
                <li><strong>Cloud Integration:</strong> Optional cloud services and backup</li>
                <li><strong>API Access:</strong> Third-party integration and customization</li>
            </ul>
            '''
        },
        {
            'id': 5,
            'title': 'Advanced IoT Security Protocols',
            'description': 'New security standards for connected devices',
            'image': 'iot-platform.jpg',
            'category': 'Security',
            'date': '2024-08-15',
            'content': 'The latest IoT security protocols provide enhanced protection for connected devices, addressing growing concerns about cybersecurity in smart systems.',
            'tags': ['Security', 'IoT', 'Protocols', 'Cybersecurity'],
            'full_content': '''
            <h3>Securing the Connected World</h3>
            <p>As IoT devices become increasingly prevalent, security has emerged as a critical concern. New protocols and standards are being developed to protect connected systems from cyber threats.</p>
            
            <h3>Key Security Challenges</h3>
            <p>IoT security faces unique challenges:</p>
            <ul>
                <li><strong>Device Diversity:</strong> Wide range of hardware and software platforms</li>
                <li><strong>Resource Constraints:</strong> Limited processing power and memory</li>
                <li><strong>Network Complexity:</strong> Multiple communication protocols</li>
                <li><strong>Lifecycle Management:</strong> Long-term security updates</li>
            </ul>
            
            <h3>New Security Protocols</h3>
            <p>Recent developments in IoT security include:</p>
            <ul>
                <li><strong>Device Authentication:</strong> Secure device identity verification</li>
                <li><strong>Encrypted Communication:</strong> End-to-end data protection</li>
                <li><strong>Secure Boot:</strong> Verified firmware loading</li>
                <li><strong>Over-the-Air Updates:</strong> Secure firmware updates</li>
            </ul>
            
            <h3>Implementation Best Practices</h3>
            <p>Organizations should implement:</p>
            <ul>
                <li>Multi-layered security architecture</li>
                <li>Regular security assessments</li>
                <li>Continuous monitoring and threat detection</li>
                <li>Employee security training</li>
            </ul>
            '''
        },
        {
            'id': 6,
            'title': '5G Integration in Industrial IoT',
            'description': 'Revolutionary connectivity solutions for industrial applications',
            'image': 'tech-network.jpg',
            'category': 'Industrial',
            'date': '2024-07-20',
            'content': '5G technology is transforming industrial IoT applications, enabling ultra-low latency communication and massive device connectivity for smart manufacturing.',
            'tags': ['5G', 'Industrial IoT', 'Manufacturing', 'Connectivity'],
            'full_content': '''
            <h3>Industrial Revolution 4.0</h3>
            <p>5G technology is ushering in a new era of industrial connectivity, enabling unprecedented levels of automation, efficiency, and intelligence in manufacturing environments.</p>
            
            <h3>5G Capabilities for Industry</h3>
            <p>5G networks provide unique advantages for industrial applications:</p>
            <ul>
                <li><strong>Ultra-Low Latency:</strong> Sub-millisecond response times</li>
                <li><strong>High Reliability:</strong> 99.999% uptime guarantees</li>
                <li><strong>Massive Connectivity:</strong> Support for millions of devices</li>
                <li><strong>High Bandwidth:</strong> Gigabit data transfer rates</li>
            </ul>
            
            <h3>Industrial Applications</h3>
            <p>5G is transforming various industrial sectors:</p>
            <ul>
                <li><strong>Smart Manufacturing:</strong> Real-time production monitoring</li>
                <li><strong>Autonomous Vehicles:</strong> Factory floor logistics</li>
                <li><strong>Remote Operations:</strong> Teleoperation of machinery</li>
                <li><strong>Predictive Maintenance:</strong> AI-powered equipment monitoring</li>
            </ul>
            
            <h3>Implementation Challenges</h3>
            <p>While promising, 5G industrial deployment faces challenges:</p>
            <ul>
                <li>Infrastructure investment requirements</li>
                <li>Spectrum allocation and management</li>
                <li>Integration with existing systems</li>
                <li>Workforce training and adaptation</li>
            </ul>
            
            <h3>Future Outlook</h3>
            <p>The integration of 5G with industrial IoT is expected to accelerate digital transformation across manufacturing sectors, enabling new business models and operational efficiencies.</p>
            '''
        }
    ]
    
    # Находим статью по ID
    article = next((article for article in news_articles if article['id'] == article_id), None)
    
    if article:
        return render_template('article.html', page='news', article=article, articles=news_articles)
    else:
        return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)