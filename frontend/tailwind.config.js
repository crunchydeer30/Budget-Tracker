/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				primary: '#3056d3',
				'primary-dark': '#2647b5',
				'font-primary': '#000',
				'font-secondary': '#637381'
			}
		}
	},
	plugins: []
};
