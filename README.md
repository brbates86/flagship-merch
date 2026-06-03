# Flagship Merch - Premium Merchandise Website

A modern, sleek website for a merchandise company built with HTML, CSS, and JavaScript. Deployed on GitHub Pages.

## Features

- **Modern Design**: Clean, minimalist design with black, gray, and white color scheme
- **Responsive**: Fully responsive design that works on all devices
- **Three Main Pages**:
  - Home: Hero section with company overview and features
  - About: Owner information and showcase of completed projects
  - Contact: Comprehensive form for potential clients with email functionality

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: GitHub Pages
- **Styling**: Custom CSS with modern design principles
- **Contact Form**: Formspree integration for form submissions

## Setup Instructions

### 1. View the Website

The website is automatically deployed on GitHub Pages at:
**https://brbates86.github.io/flagship-merch/**

### 2. Local Development

To run locally, simply open `index.html` in your browser or use a simple HTTP server:

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

### 3. Contact Form Setup

The contact form uses Formspree for handling submissions. To set up:

1. Go to [Formspree.io](https://formspree.io)
2. Create a free account
3. Create a new form
4. Replace `YOUR_FORM_ID` in `contact.html` with your Formspree form ID
5. Commit and push changes

## Project Structure

```
flagship-merch/
├── index.html          # Homepage
├── about.html          # About page with owner info and projects
├── contact.html        # Contact form page
├── styles.css          # Main stylesheet
├── script.js           # JavaScript functionality
├── app.py              # Flask backend application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Features Breakdown

### Homepage (`index.html`)
- Hero section with compelling messaging
- Features grid highlighting company strengths
- Call-to-action section
- Modern navigation with mobile hamburger menu

### About Page (`about.html`)
- Company story and mission
- Owner/Founder information section
- Showcase of completed projects
- Company values and approach

### Contact Page (`contact.html`)
- Comprehensive contact form with fields for:
  - Personal information
  - Project details
  - Budget and timeline
  - Detailed project description
- Form validation and submission handling
- Email integration for notifications

### Styling (`styles.css`)
- Modern, clean design with black/gray/white color scheme
- Responsive grid layouts
- Smooth animations and transitions
- Mobile-first responsive design
- Professional typography using Inter font

### JavaScript (`script.js`)
- Mobile navigation toggle
- Smooth scrolling
- Form validation
- Scroll animations
- Dynamic navbar styling

### Backend (`app.py`)
- Flask web server
- Static file serving
- Form submission handling
- SMTP email integration
- Error handling and validation

## Customization

### Updating Content
1. **Owner Information**: Edit the about.html file to update owner details
2. **Projects**: Modify the projects grid in about.html to showcase your work
3. **Contact Information**: Update email and phone numbers in the footer sections
4. **Company Information**: Change company name, taglines, and descriptions throughout the HTML files

### Styling Changes
- Modify `styles.css` to adjust colors, fonts, spacing, or layout
- The color scheme is defined using CSS custom properties for easy updates
- All responsive breakpoints are clearly marked in the CSS

### Email Configuration
- Update the SMTP settings in `app.py` for different email providers
- Modify the email template in the `submit_form()` function
- Add additional form fields by updating both the HTML form and Python handler

## Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Set up proper environment variables
4. Configure a reverse proxy (nginx)
5. Use HTTPS for security

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This project is created for Flagship Merch. All rights reserved.
