import Footer from "../components/common/main/Footer";
import Navbar from "../elements/navbar/Navbar";

export default function Page() {
    return (
        <main className="min-h-screen bg-gray-50 flex flex-col">
            {/* Navbar */}
            <Navbar />

            {/* Page Content */}
            <section className="flex flex-col items-center justify-center flex-grow">
                <h1 className="text-4xl font-extrabold text-gray-900 mb-4">
                    Welcome to <span className="text-blue-600">FlirtyFly</span>
                </h1>
                <p className="text-gray-600 text-lg max-w-xl text-center">
                    A modern Next.js + Tailwind setup with reusable components.
                </p>
            </section>

            {/* Footer */}
            <Footer />
        </main>
    )
}