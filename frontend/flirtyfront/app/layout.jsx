import "./global.css";
import { Toaster } from 'react-hot-toast'

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>
                <Toaster
                    position="top-center"
                    toastOptions={{
                        success: {
                            style: { background: "#4ade80", color: "#fff" }
                        },
                        error: {
                            style: { background: "#f87171", color: "#fff" }
                        }
                    }}
                />
                {children}
            </body>
        </html>
    )
}