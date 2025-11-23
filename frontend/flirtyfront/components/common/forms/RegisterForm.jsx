"use client";

import { useState } from "react";
import Image from "next/image";

export default function RegisterForm() {
    const [formData, setFormData] = useState({
        email: "",
        phone: "",
        username: "",
        password: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Submitted:", formData);
    };

    const handleGoogleLogin = () => {
        console.log("Google Sign-In clicked");
    };

    return (
        <div className="w-full flex items-center justify-center py-10">
            <div className="bg-white shadow-xl rounded-3xl p-10 max-w-5xl w-full flex flex-col md:flex-row gap-10">

                {/* Left Illustration */}
                <div className="hidden md:flex w-1/2 items-center justify-center">
                    <Image
                        src="/auth/illustration.svg"
                        alt="Register Illustration"
                        width={350}
                        height={350}
                        className="object-contain"
                    />
                </div>

                {/* Right Form */}
                <div className="w-full md:w-1/2">
                    <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
                        Create Your Account
                    </h2>

                    {/* Form */}
                    <form onSubmit={handleSubmit} className="space-y-5">

                        {/* Username */}
                        <div>
                            <label className="text-gray-700">Username</label>
                            <input
                                type="text"
                                name="username"
                                onChange={handleChange}
                                value={formData.username}
                                placeholder="Enter your username"
                                className="w-full mt-1 px-4 py-2 border-2 border-blue-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
                                required
                            />
                        </div>

                        {/* Email */}
                        <div>
                            <label className="text-gray-700">Email</label>
                            <input
                                type="email"
                                name="email"
                                onChange={handleChange}
                                value={formData.email}
                                placeholder="Enter your email"
                                className="w-full mt-1 px-4 py-2 border-2 border-blue-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
                                required
                            />
                        </div>

                        {/* Phone */}
                        <div>
                            <label className="text-gray-700">Phone</label>
                            <input
                                type="tel"
                                name="phone"
                                onChange={handleChange}
                                value={formData.phone}
                                placeholder="Enter your phone number"
                                className="w-full mt-1 px-4 py-2 border-2 border-blue-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
                                required
                            />
                        </div>

                        {/* Password */}
                        <div>
                            <label className="text-gray-700">Password</label>
                            <input
                                type="password"
                                name="password"
                                onChange={handleChange}
                                value={formData.password}
                                placeholder="Enter your password"
                                className="w-full mt-1 px-4 py-2 border-2 border-blue-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
                                required
                            />
                        </div>

                        {/* Sign Up Button */}
                        <button
                            type="submit"
                            className="w-full py-3 rounded-xl bg-blue-600 text-white font-medium hover:bg-blue-700 transition mt-2"
                        >
                            Sign Up
                        </button>
                    </form>

                    {/* Divider */}
                    <div className="my-5 flex items-center gap-3">
                        <span className="flex-grow h-px bg-gray-300"></span>
                        <span className="text-gray-500 text-sm">OR</span>
                        <span className="flex-grow h-px bg-gray-300"></span>
                    </div>

                    {/* Google Sign-In */}
                    <button
                        onClick={handleGoogleLogin}
                        className="w-full py-3 border rounded-xl flex items-center justify-center gap-3 hover:bg-gray-50 transition cursor-pointer"
                    >
                        <Image src="/icons/google.svg" alt="Google" width={25} height={25} />
                        <span className="text-gray-700">Continue with Google</span>
                    </button>

                    {/* Already have an account */}
                    <p className="text-sm text-gray-600 text-center mt-6">
                        Already have an account?{" "}
                        <a href="/users/login" className="text-blue-600 hover:underline">
                            Sign In
                        </a>
                    </p>
                </div>
            </div>
        </div>
    );
}
