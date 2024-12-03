%define major %(echo %{version} |cut -d. -f1)
%define oldlibname %mklibname z3 4
%define libname %mklibname z3
%define devname %mklibname z3 -d

# z3's cmake files generate dependencies on cmake(GMP)
# [which is provided by KDE 5's KDELibs4Support, not as you may think GMP]
# and cmake(Threads) which is provided by cmake, not glibc...
%define __requires_exclude .*cmake.*

Name:		z3
Version:	4.13.3
Release:	2
Summary:	The Z3 Theorem Prover
Source0:	https://github.com/Z3Prover/z3/archive/refs/tags/z3-%{version}.tar.gz
License:	MIT
Requires:	%{libname} = %{EVRD}
BuildRequires:	cmake
BuildRequires:	ninja

%description
Z3 Theorem Prover is a satisfiability modulo theories (SMT) solver.

Z3 supports arithmetic, fixed-size bit-vectors, extensional arrays,
datatypes, uninterpreted functions, and quantifiers. Its main
applications are extended static checking, test case generation,
and predicate abstraction.

%package -n %{libname}
Summary:	Library for the Z3 Theorem Prover
Group:		System/Libraries
# Renamed before 6.0
%rename %{oldlibname}

%description -n %{libname}
Library for the Z3 Theorem Prover

%package -n %{devname}
Summary:	Development files for the Z3 Theorem Prover
Group:		Development/C
# In place of the cmake(GMP) requirements
# we filter out with __requires_exclude
Requires:	pkgconfig(gmp)

%description -n %{devname}
Development files for the Z3 Theorem Prover

%prep
%autosetup -p1 -n z3-z3-%{version}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/z3

%files -n %{libname}
%{_libdir}/libz3.so.%{major}*

%files -n %{devname}
%{_libdir}/libz3.so
%{_includedir}/*.h
%{_libdir}/cmake/z3
%{_libdir}/pkgconfig/z3.pc
