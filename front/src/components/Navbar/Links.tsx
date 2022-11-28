import { Link } from "react-router-dom";

interface LinksProps {
  linkName: string
  href?: string
}

export function Links({ linkName = "Error", href = "" }: LinksProps) {
  return (
    <div className="py-2">
      <Link to={href} className="hover:text-pink-500  md:visible lg:visible">
        {linkName}
      </Link>
    </div>
  );
};
