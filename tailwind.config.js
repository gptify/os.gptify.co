module.exports = {
  content: [
    './**/*.html',
    './**/*.py',
    '../*.html',
    '../*.py'
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        serif: ['"Instrument Serif"', 'Georgia', 'serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
        poppins: ['"Poppins"', 'sans-serif'],
      },
      colors: {
        paper: '#FAF9F5',
        surface: '#FFFFFF',
        subtle: '#F4F2EC',
        divider: '#E7E5DF',
        dividerDark: '#D8D5CD',
        slateDark: '#0F172A',
        slateMuted: '#64748B',
        emeraldBrand: '#087F6A',
        emeraldDark: '#066352',
        emeraldLight: '#ECFDF5',
        limeSpark: '#B7F34A',
        amberBrand: '#D97706',
        skyBrand: '#0284C7',
        purpleBrand: '#7C3AED',
        indigoBrand: '#4F46E5',
      }
    }
  }
};
