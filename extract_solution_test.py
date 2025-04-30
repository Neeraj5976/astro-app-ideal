import os
from extract_solution import extract_solution

llm_response = '''

```javascript
//   /src/components/BlogCard.astro

---
interface Props {
  title: string;
  description: string;
  date: string;
  author: string;
  image: string;
}

const { 
  title = 'Untitled Post',
  description = 'No description available',
  date = 'No date',
  author = 'Anonymous',
  image = '/placeholder-image.jpg'
} = Astro.props;
---

<div class="blog-card" data-testid="blog-card">
  <div class="blog-card-header" data-testid="card-header">
    <img src={image} alt={title} class="blog-card-image" data-testid="card-image" />
    <h2 class="blog-card-title" data-testid="card-title">{title}</h2>
  </div>
  <div class="blog-card-content" data-testid="card-content">
    <p class="blog-card-description" data-testid="card-description">{description}</p>
    <div class="blog-card-meta">
      <span class="blog-card-date" data-testid="card-date">{date}</span>
      <span class="blog-card-author" data-testid="card-author">By {author}</span>
    </div>
  </div>
  <button class="blog-card-toggle" data-testid="toggle-button">Read More</button>
</div>

<style>
  .blog-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 16px 0;
    padding: 16px;
    transition: all 0.3s ease;
  }

  .blog-card-header {
    margin-bottom: 1rem;
  }

  .blog-card-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 4px;
  }

  .blog-card-title {
    margin: 1rem 0;
    font-size: 1.5rem;
    color: #333;
  }

  .blog-card-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
  }

  .blog-card.expanded .blog-card-content {
    max-height: 1000px;
  }

  .blog-card-description {
    color: #666;
    line-height: 1.6;
  }

  .blog-card-meta {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
    color: #888;
    font-size: 0.9rem;
  }

  .blog-card-toggle {
    background: #0056b3;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
    transition: background 0.3s ease;
  }

  .blog-card-toggle:hover {
    background: #003d80;
  }
</style>

<script>
  document.querySelectorAll('.blog-card-toggle').forEach(button => {
    button.addEventListener('click', () => {
      const card = button.closest('.blog-card');
      if (card) {
        card.classList.toggle('expanded');
        button.textContent = card.classList.contains('expanded') ? 'Read Less' : 'Read More';
      }
    });
  });
</script> 
```

```javascript
//   /src/pages/index.astro

---
import BaseHead from '../components/BaseHead.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import { SITE_TITLE, SITE_DESCRIPTION } from '../consts';
import BlogCard from '../components/BlogCard.astro';
import  blogPosts  from '../data/blogPosts';
---

<!doctype html>
<html lang="en">
	<head>
		<BaseHead title={SITE_TITLE} description={SITE_DESCRIPTION} />
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Web Blog</title>
	</head>
	<body>
		<Header />
		<main>
			<h1>Web Technology Blog</h1>
			<div class="blog-grid" data-testid="blog-grid">
				{blogPosts.length === 0 ? (
					<p data-testid="no-posts-message">No blog posts available</p>
				) : (
					blogPosts.map((post) => (
						<BlogCard
							title={post.title}
							description={post.description}
							date={post.date}
							author={post.author}
							image={post.image}
						/>
					))
				)}
			</div>
		</main>
		<Footer />
	</body>
</html>

<style>
	body {
		font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		line-height: 1.6;
		color: #333;
		max-width: 1200px;
		margin: 0 auto;
		padding: 2rem;
		background: #f5f5f5;
	}

	h1 {
		text-align: center;
		margin-bottom: 2rem;
		color: #2c3e50;
	}

	.blog-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		gap: 2rem;
		padding: 1rem;
	}

	@media (max-width: 768px) {
		.blog-grid {
			grid-template-columns: 1fr;
		}
	}
</style>

```

```javascript
//   /src/data/blogPosts.ts


interface BlogPost {
  title: string;
  description: string;
  date: string;
  author: string;
  image: string;
  }
  
  const blogPosts: BlogPost[] = [
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
  
  export default blogPosts;
```

'''

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError(
            "Expected response to be a list of (file_name, code) tuples.")

    for item in response:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item
        
        # Create the directory if it doesn't exist
        directory = os.path.dirname(file_name)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Write the file
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
