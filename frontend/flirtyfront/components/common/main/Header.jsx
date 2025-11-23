export default function Header() {
    return (
        <nav className="flex items-center justify-between px-8 py-4 bg-white shadow">
            {/* Logo */}
            <div className="text-2xl font-bold text-blue-600">FlirtyFly</div>

            {/* Links */}
            <div className="hidden md:flex space-x-6">
                <a href="#" className="text-gray-700 hover:text-blue-600">Home</a>
                <a href="#" className="text-gray-700 hover:text-blue-600">About</a>
                <a href="#" className="text-gray-700 hover:text-blue-600">Services</a>
                <a href="#" className="text-gray-700 hover:text-blue-600">Contact</a>
            </div>

            {/* Buttons */}
            <div className="flex space-x-4">
                <button className="px-4 py-2 rounded-lg border border-blue-600 text-blue-600 hover:bg-blue-50 transition">
                    Login
                </button>
                <button className="px-4 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition">
                    Register
                </button>
            </div>
        </nav>
    );
}
