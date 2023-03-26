/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.html"],
  theme: {
    extend: {
        colors: {
            "letterboxd":{
                1:"#14171C",
                2:"#2C343F",
                3:"#556678",
                4:"#00B021",
                5:"#F27405"
            }
        },
    },
  },
  plugins: [],
}
