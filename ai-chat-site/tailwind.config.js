/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.{js,ts}"
  ],
  theme: {
    extend: {
      colors: {
        primary: "#f9f506",
        "background-light": "#f8f8f5",
        "background-dark": "#23220f",
        "sidebar-light": "#f2f2ee",
        "sidebar-dark": "#1c1b0a",
      },
      fontFamily: {
        display: ["Spline Sans", "sans-serif"],
      },
      borderRadius: {
        DEFAULT: "1rem",
        lg: "2rem",
        xl: "3rem",
        full: "9999px",
      },
    },
  },
  plugins: [],
};
