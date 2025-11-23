import React from 'react'
import Navbar from '../../../elements/navbar/Navbar'
import LoginForm from '../../../components/common/forms/LoginForm'
import Footer from '../../../components/common/main/Footer'

export default function page() {
    return (
        <main className="min-h-screen flex flex-col">

            {/* Top Navbar */}
            <Navbar />

            {/* Center Content */}
            <div className="flex-1 flex items-center justify-center py-10">
                <LoginForm />
            </div>

            {/* Bottom Footer */}
            <Footer />
        </main>
    )
}
