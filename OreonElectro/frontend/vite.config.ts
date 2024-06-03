import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import axios from 'axios'

export default defineConfig({
	plugins: [react()],
	server: {
		proxy: {
			'/api': {
				target: 'http://127.0.0.1:8000',
				changeOrigin: true,
				secure: false,
				options: {
					headers: {
						'Access-Control-Allow-Origin': 'http://localhost:3000',
						'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
						'Access-Control-Allow-Headers': 'Content-Type',
					},
				},
			},
		},
	},
})
