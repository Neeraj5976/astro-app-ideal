export interface BlogPost {
  title: string;
  description: string;
  date: string;
  author: string;
  image: string;
}

export const blogPosts: BlogPost[] = [
  {
    title: "Getting Started with Astro",
    description: "Learn how to build fast, content-focused websites with Astro. This guide covers the basics of Astro, its features, and how to get started with your first project.",
    date: "2024-03-15",
    author: "John Doe",
    image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "The Future of Web Development",
    description: "Explore the latest trends and technologies shaping the future of web development. From AI to WebAssembly, discover what's next in the world of web.",
    date: "2024-03-14",
    author: "Jane Smith",
    image: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "Building Responsive Designs",
    description: "Master the art of creating responsive web designs that work beautifully across all devices. Learn best practices and techniques for modern responsive design.",
    date: "2024-03-13",
    author: "Mike Johnson",
    image: "https://images.unsplash.com/photo-1547658719-da2b51169166?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "JavaScript Best Practices",
    description: "Discover essential JavaScript best practices that will help you write cleaner, more maintainable code. From ES6+ features to design patterns.",
    date: "2024-03-12",
    author: "Sarah Wilson",
    image: "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "CSS Grid Layout",
    description: "A comprehensive guide to CSS Grid Layout. Learn how to create complex layouts with ease using this powerful CSS feature.",
    date: "2024-03-11",
    author: "David Brown",
    image: "https://images.unsplash.com/photo-1507721999472-8ed4421c4af2?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "Web Performance Optimization",
    description: "Learn how to optimize your website's performance. From image optimization to code splitting, discover techniques to make your site faster.",
    date: "2024-03-10",
    author: "Emily Davis",
    image: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "TypeScript Fundamentals",
    description: "Get started with TypeScript. Learn about types, interfaces, and how to use TypeScript to write more robust JavaScript code.",
    date: "2024-03-09",
    author: "Alex Turner",
    image: "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&auto=format&fit=crop&q=60"
  },
  {
    title: "Modern CSS Techniques",
    description: "Explore modern CSS techniques and features. From CSS variables to Flexbox, learn how to create stunning layouts with CSS.",
    date: "2024-03-08",
    author: "Lisa Anderson",
    image: "https://images.unsplash.com/photo-1507721999472-8ed4421c4af2?w=800&auto=format&fit=crop&q=60"
  }
]; 