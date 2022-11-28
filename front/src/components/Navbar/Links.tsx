interface LinksProps {
  linkName: string
  href?: string
}

export function Links({ linkName = "Error", href = "" }: LinksProps) {
  return (
    <div className="py-2">
      <a className="hover:text-pink-500  md:visible lg:visible" href={href}>
        {linkName}
      </a>
    </div>
  );
};
