import Image from "next/image";
import {NavbarDemo} from "./components/Navbar/Navbar";
import {AuroraBackgroundDemo} from "./components/Header/Header";
import {GoogleGeminiEffectDemo} from "./components/Gemini"
import {AnimatedPinDemo} from "./components/Features/Feature1";
import {HeroParallaxDemo} from "./components/Header/HeroParallax";
import { LampDemo } from "./components/Features/Feature2";
// import {Footer} from "./components/Footer/Footer";
export default function Home() {
  return (<>
    {/* <HeroParallaxDemo/> */}
    <LampDemo />
    
    <AuroraBackgroundDemo/>
    <AnimatedPinDemo/>
    {/* <Footer/> */}
    {/* <GoogleGeminiEffectDemo/> */}
    </>
    );
}
