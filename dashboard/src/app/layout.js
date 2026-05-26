import { Outfit } from "next/font/google";
import "./globals.css";

const outfit = Outfit({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800"],
});

export const metadata = {
  title: "Creador de Mensajes Positivos - Dashboard",
  description: "Panel de control premium y chat interactivo con el Agente de Crecimiento Personal.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="es" className="h-full">
      <body className={`${outfit.className} min-h-full flex flex-col`}>
        {children}
      </body>
    </html>
  );
}

