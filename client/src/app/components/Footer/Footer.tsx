// // Import React
// import React from 'react';

// // Import the Typography component
// import { Typography } from "@material-tailwind/react";

// // Define the LINKS array
// const LINKS = [
//   {
//     title: "Product",
//     items: ["Overview", "Features", "Solutions", "Tutorials"],
//   },
//   {
//     title: "Company",
//     items: ["About us", "Careers", "Press", "News"],
//   },
//   {
//     title: "Resource",
//     items: ["Blog", "Newsletter", "Events", "Help center"],
//   },
// ];

// // Get the current year
// const currentYear = new Date().getFullYear();

// // Define the FooterWithSocialLinks component
// export function Footer() {
//   return (
//     <footer className="relative w-full">
//       <div className="mx-auto w-full max-w-7xl px-8">
//         <div className="grid grid-cols-1 justify-between gap-4 md:grid-cols-2">
//           <Typography variant="h5" className="mb-6">
//             Material Tailwind
//           </Typography>
//           <div className="grid grid-cols-3 justify-between gap-4">
//             {LINKS.map(({ title, items }) => (
//               <ul key={title}>
//                 <Typography
//                   variant="small"
//                   color="blue-gray"
//                   className="mb-3 font-medium opacity-40"
//                 >
//                   {title}
//                 </Typography>
//                 {items.map((link) => (
//                   <li key={link}>
//                     <Typography
//                       as="a"
//                       href="#"
//                       color="gray"
//                       className="py-1.5 font-normal transition-colors hover:text-blue-gray-900"
//                     >
//                       {link}
//                     </Typography>
//                   </li>
//                 ))}
//               </ul>
//             ))}
//           </div>
//         </div>
//         <div className="mt-12 flex w-full flex-col items-center justify-center border-t border-blue-gray-50 py-4 md:flex-row md:justify-between">
//           <Typography
//             variant="small"
//             className="mb-4 text-center font-normal text-blue-gray-900 md:mb-0"
//           >
//             &copy; {currentYear} <a href="https://material-tailwind.com/">Material Tailwind</a>. All
//             Rights Reserved.
//           </Typography>
//           <div className="flex gap-4 text-blue-gray-900 sm:justify-center">
//             <Typography as="a" href="#" className="opacity-80 transition-opacity hover:opacity-100">
//               {/* SVG Icons */}
//             </Typography>
//             {/* Add other social icons as needed */}
//           </div>
//         </div>
//       </div>
//     </footer>
//   );
// }
