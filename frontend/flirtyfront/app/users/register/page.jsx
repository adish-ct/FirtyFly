import RegisterForm from "../../../components/common/forms/RegisterForm";
import Footer from "../../../components/common/main/Footer";
import Navbar from "../../../elements/navbar/Navbar";

export default function page() {
    return (
        <main>
            <Navbar />
            <RegisterForm />
            <Footer />
        </main>
    )
}
