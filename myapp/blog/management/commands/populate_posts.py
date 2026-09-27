import random
from blog.models import Post , Category 
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any): 
        # Delete existing data
        Post.objects.all().delete()

        titles = [
            "Engineer evolves rapidly every year",
            "Cloud computing changes business operations",
            "Cybersecurity protects our digital data",
            "Artificial intelligence simplifies complex tasks",
            "Programming languages build modern software",
            "Networks connect devices and people",
            "Big data drives smart decisions",
            "IT support ensures system uptime",
            "Data analytics improves business strategies",
            "Machine learning enhances user experience",
            "Digital tools boost workplace productivity",
            "Software updates fix security issues",
            "Web development powers online presence",
            "Mobile apps transform daily life",
            "Internet speeds influence user behavior",
            "Blockchain secures financial digital transactions",
            "Remote work relies on IT",
            "Databases store and retrieve information",
            "Information systems streamline organizational processes",
            "Smart devices use advanced technology",
        ]

        contents = [
            
    "Information technology transforms the way businesses operate by automating processes, increasing operational speed, and enhancing connectivity, enabling organizations to work more efficiently and compete in a global digital environment",
    "Cloud computing provides scalable storage and high-performance processing capabilities, allowing businesses to manage their digital infrastructure flexibly, reduce costs, and adapt quickly to changing demands",
    "Cybersecurity plays a critical role in protecting sensitive data from unauthorized access, breaches, and online threats, ensuring that both businesses and individuals remain secure in the digital world",
    "Machine learning empowers organizations to make better decisions by identifying patterns in vast datasets, enabling predictive insights and innovative, data-driven solutions",
    "Big data analytics uncovers valuable trends and patterns hidden within large volumes of information, helping businesses understand customer behavior and improve their strategic planning",
    "Networking connects devices, systems, and applications to facilitate seamless communication, data sharing, and collaboration across local and global platforms",
    "Blockchain technology ensures secure, transparent, and tamper-proof transactions by using decentralized verification methods, making it a trusted solution for finance, supply chains, and digital services",
    "Artificial intelligence mimics human thought processes to automate tasks, analyze information, and create intelligent systems capable of learning and adapting over time",
    "IT support is essential for keeping technology systems running smoothly by diagnosing and fixing issues, providing maintenance, and assisting users with technical challenges",
    "Mobile applications improve user engagement by offering convenient, interactive, and personalized digital experiences accessible from anywhere at any time",
    "Programming languages are the foundation of software development, enabling the creation of applications, automation of processes, and development of innovative digital solutions",
    "Web development builds responsive, user-friendly websites that provide engaging online experiences, making information and services easily accessible to a global audience",
    "Databases store, organize, and retrieve structured digital information efficiently, ensuring that critical data remains accurate, secure, and accessible when needed",
    "The Internet of Things (IoT) connects physical devices to the internet, enabling remote monitoring, automation, and smarter decision-making across industries",
    "IT policies establish guidelines for the safe and responsible use of technology, helping organizations maintain security, compliance, and ethical digital practices",
    "Data centers house the essential infrastructure that supports enterprise IT operations, cloud services, and mission-critical systems, ensuring reliability and uptime",
    "Digital transformation integrates advanced technologies into business operations, driving innovation, improving productivity, and enabling faster responses to market changes",
    "Software engineering focuses on designing reliable, scalable, and maintainable applications that meet user needs and support long-term technological growth",
    "IT professionals provide expertise in solving technical problems, optimizing systems, and implementing solutions that align with business objectives",
    "Information systems combine people, processes, and technology into a unified structure that supports decision-making, operational efficiency, and overall organizational success"
]
        

        img_urls = [
            f"https://picsum.photos/id/{i}/800/400" for i in range(1, 21)
        ]
  
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            post = Post(title=title, content=content, img_url=img_url, category=category)
            post.save()

        self.stdout.write(self.style.SUCCESS("Successfully inserted 20 posts"))