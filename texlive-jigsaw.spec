%global tl_name jigsaw
%global tl_revision 71923

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Draw jigsaw pieces with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/jigsaw
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jigsaw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jigsaw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(epstopdf-pkg)
Requires:	texlive(iftex)
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a small LaTeX package to draw jigsaw pieces with TikZ. It is
possible to draw individual pieces and adjust their shape, create tile
patterns or automatically generate complete jigsaws.

