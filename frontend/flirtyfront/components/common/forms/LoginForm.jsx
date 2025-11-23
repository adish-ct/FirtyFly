"use client";

import { useState } from "react";
import Image from "next/image";
import { loginUser } from "../../../lib/api/authApi";
import toast from "react-hot-toast";
import { useRouter } from "next/navigation";

export default function LoginForm() {
    const router = useRouter();

    const [formData, setFormData] = useState({
        username: "",
        password: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await loginUser(formData);
            if (response) {

                localStorage.setItem("access_token", response?.data?.access_token);
                toast.success("🎉 Login Successful!");
            }

            setTimeout(() => {
                router.push("/dashboard");
            }, 1000);

        } catch (error) {
            toast.error(error?.response?.data?.detail || "Invalid credentials");
        }
    };

    const handleGoogleLogin = () => {
        console.log("Google login clicked");
    };

    const isDisabled = !formData.username || !formData.password;

    return (
        <div className="w-full flex items-center justify-center py-10">
            <div className="bg-white shadow-xl rounded-3xl p-10 max-w-5xl w-full flex flex-col md:flex-row gap-10">

                {/* Left Illustration (MATCHING REGISTER FORM) */}
                <div className="hidden md:flex w-1/2 items-center justify-center">
                    <Image
                        src="/auth/login-illustration.svg"
                        alt="Login Illustration"
                        width={350}
                        height={350}
                        className="object-contain"
                    />
                </div>

                {/* Right Form */}
                <div className="w-full md:w-1/2">
                    <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
                        Sign In to Your Account
                    </h2>

                    {/* FORM */}
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
                                className="w-full mt-1 px-4 py-2 border-2 border-blue-200 rounded-xl
                                           focus:outline-none focus:ring-2 focus:ring-blue-500"
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
                                className="w-full mt-1 px-4 py-2 border-2 border-blue-200 rounded-xl 
                                           focus:outline-none focus:ring-2 focus:ring-blue-500"
                                required
                            />
                            <p className="mt-1 text-right">
                                <a href="#" className="text-sm text-blue-600 hover:underline">
                                    Forgot your password?
                                </a>
                            </p>
                        </div>

                        {/* Login Button */}
                        <button
                            type="submit"
                            disabled={isDisabled}
                            className={`
                                        w-full py-3 rounded-xl font-medium mt-2 transition
                                        ${isDisabled
                                    ? "bg-blue-300 cursor-not-allowed opacity-60"
                                    : "bg-blue-600 text-white hover:bg-blue-700"
                                }
                                    `}
                        >
                            Log In
                        </button>
                    </form>

                    {/* Divider */}
                    <div className="my-5 flex items-center gap-3">
                        <span className="flex-grow h-px bg-gray-300"></span>
                        <span className="text-gray-500 text-sm">OR</span>
                        <span className="flex-grow h-px bg-gray-300"></span>
                    </div>

                    {/* Google Login */}
                    <button
                        onClick={handleGoogleLogin}
                        className="w-full py-3 border rounded-xl flex items-center justify-center gap-3 
                                   hover:bg-gray-50 transition cursor-pointer"
                    >
                        <Image src="/icons/google.svg" alt="Google" width={25} height={25} />
                        <span className="text-gray-700">Continue with Google</span>
                    </button>

                    {/* Register Link */}
                    <p className="text-sm text-gray-600 text-center mt-6">
                        Don’t have an account?{" "}
                        <a href="/users/register" className="text-blue-600 hover:underline">
                            Sign Up
                        </a>
                    </p>
                </div>
            </div>
        </div >
    );
}
