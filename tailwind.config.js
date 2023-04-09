/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*{.html,js,py}"],
  theme: {
    extend: {
        colors: {
            "letterboxd":{
                1:"#14171C",
                2:"#2C343F",
                3:"#556678",
                4:"#00B021",
                5:"#F27405",
               6:"#CCDDED",
            }
        },
        fontFamily:{
            'myfont':['myfont','sans-serif'],
            'myfontLight':['myfontlight','sans-serif'],
            'abrilbold':['abrilbold','sans-serif'],
            'abril' : ['abril','sans-serif'],
            'starrating' : ['star-rating','sans-serif']
        }
    },
  },
  plugins: [
    require("tailwind-gradient-mask-image"),
    require('tailwind-scrollbar'),
  ],
}
