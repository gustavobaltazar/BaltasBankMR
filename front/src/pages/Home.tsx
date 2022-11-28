import { DarkMode } from '../components/DarkmodeControl/Darkmode'
import { Navbar } from '../components/Navbar/Navbar.jsx'
import { Content } from '../components/Content/Content.jsx'
export function Home() {
    document.title = 'Homepage'

    return (
        <>
            <Navbar />
            <Content />
        </>
    )
}