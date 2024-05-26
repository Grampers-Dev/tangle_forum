import globals from "globals";
import pluginJs from "@eslint/js";

export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "commonjs",
      globals: {
        ...globals.browser,
        $: "readonly",
        jQuery: "readonly",
        gsap: "readonly"
      }
    }
  },
  pluginJs.configs.recommended,
];
