import "vuetify/styles";
import { createVuetify } from "vuetify";
import { md3 } from "vuetify/blueprints";

export default createVuetify({
  blueprint: md3,
  theme: {
    defaultTheme: "spaceTheme",
    themes: {
      spaceTheme: {
        dark: false,
        colors: {
          background: "#f6f4ef",
          surface: "#ffffff",
          primary: "#0b2f5b",
          secondary: "#cf5c36",
          accent: "#3a7d44",
          info: "#1f6feb",
        },
      },
    },
  },
});
