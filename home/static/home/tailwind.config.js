/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../../templates/home/*.html"],
    theme: {
        extend: {
            colors: {
                pri: '#ffffff',
                sec: '#1a2027',
                acc: '#948397',
            } 
        }, 
    },
    plugins: [],
};
