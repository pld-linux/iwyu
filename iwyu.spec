%define	llvm_ver	21

Summary:	Include What You Use - tool for use with clang to analyze includes in C and C++ source files
Summary(pl.UTF-8):	Include What You Use - narzędzie dla clanga do analizy plików włączanych przez pliki źródłowe w C i C++
Name:		iwyu
# 0.21.x for llvm 17, 0.22.x for llvm 18 etc.
Version:	0.25
Release:	1
License:	LLVM (BSD-like)
Group:		Development/Tools
#Source0Download: https://github.com/include-what-you-use/include-what-you-use/releases
Source0:	https://github.com/include-what-you-use/include-what-you-use/archive/%{version}/include-what-you-use-%{version}.tar.gz
# Source0-md5:	91122441a3fbd8194a925c8b2a0bcc9d
URL:		https://github.com/include-what-you-use/include-what-you-use
BuildRequires:	clang-devel >= %{llvm_ver}
BuildRequires:	cmake >= 3.20.0
BuildRequires:	llvm-devel >= %{llvm_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Include what you use" means this: for every symbol (type, function,
variable, or macro) that you use in foo.cc (or foo.cpp), either
foo.cc or foo.h should include a .h file that exports the declaration
of that symbol. (Similarly, for foo_test.cc, either foo_test.cc or
foo.h should do the including.)  Obviously symbols defined in foo.cc
itself are excluded from this requirement.

%description -l pl.UTF-8
"Include what you use" (włączaj to, czego używasz) oznacza, że dla
każdego symbolu (typu, funkcji, zmiennej, makra) używanego w foo.cc
(lub foo.cpp) plik foo.cc lub foo.h powinien włączać plik .h
eksportujący deklarację tego symbolu (podobnie, w przypadku
foo_test.cc albo foo_test.cc, albo foo.h powinien zawierać włączenie).
Oczywiście symbole zdefiniowane w samym foo.cc są wykluczone z tego
wymagania.

%prep
%setup -q -n include-what-you-use-%{version}

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' fix_includes.py iwyu_tool.py

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT README.md
%attr(755,root,root) %{_bindir}/fix_includes.py
%attr(755,root,root) %{_bindir}/include-what-you-use
%attr(755,root,root) %{_bindir}/iwyu_tool.py
%{_datadir}/include-what-you-use
%{_mandir}/man1/include-what-you-use.1*
