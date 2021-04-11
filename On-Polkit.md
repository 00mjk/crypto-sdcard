## On admin configurable policy rules with Polkit v0.1xy

### 1. History of Polkit's admin configurable policy rules

[This article](https://www.admin-magazine.com/Articles/Assigning-Privileges-with-sudo-and-PolicyKit) nicely (and simply) explains the intention and functionality of Polkit.

#### 1.1. Polkit ≤ 0.105 versus Polkit ≥ 0.106 WRT admin configured policy rules

* **Polkit 0.106 switched from the ".pkla (Policy Kit Local Authority / [pklocalauthority](https://www.freedesktop.org/software/polkit/docs/0.105/pklocalauthority.8.html))" file format to a JavaScript-based ".rules" configuration file format**
  
  See the [original announcement and explanation](https://davidz25.blogspot.com/2012/06/authorization-rules-in-polkit.html) for this change.<br />
  The comments at this page concisely reflect the year long debates this change triggered, including most of the technical and usablility issues denoted.<br />
  Note that there was no migration period (in which both file formats were supported): Polkit ≤ 0.105 solely understands ".pkla" files, while Polkit ≥ 0.106 only understands JavaScript-based ".rules" files.  See their fundamental differences [in this example](https://fossies.org/linux/libvirt/docs/auth.rst#unix-socket-policykit-auth).

* **Consequences / effects for Linux distributions**
  
  Aside of all usability issues (mainly JavaScript not being among the repertoire of an UNIX admin) and a programming languagage ("touring complete") being unsuitable and problematic to dangerous for configuration files (see sendmail.cf and some other (hi)stories), requiring a JavaScript interpreter as a fundamental depencendcy and needed early at the system start is the major technical issue: [This Ubuntu bug summarises it well](https://bugs.launchpad.net/ubuntu/+source/policykit-1/+bug/1086783).
  
  Consequently most Linux distributions stayed with Polkit 0.105 for a while and then started to take different approaches, often multiple of them temporally staggered:
  1. Backport fixes and even some new fuctionality from newer Polkit releases, creating Polkit 0.105-z versions.
  2. Create tools to automatically convert policy rules in the ".pkla" file format to the ".rules" file format.
  3. Extend the recent Polkit to parse ".pkla" files, e.g. by the [polkit-pkla-compat](https://pagure.io/polkit-pkla-compat) helper.
  4. Rewrite all distribution specific policy rules as ".rules" files (by the help from tools denoted in point ii above) and completly switch to recent Polkit releases: Users of these distributions have to do the same for their own policy rules, then.

* **Polkit versions in SailfishOS**
  
  As with some other components, SailfishOS tends to lag behind recent Polkit releases, which is not neccesarily a bad thing.<br />
  SailfishOS 2.2.0 deployed Polkit 0.104, some later release (before SailfishOS 3.2.1) switched to Polkit 0.105 and SailfishOS 4.0.1 is still deploying Polkit 0.105.<br />
  This looks like aforementioned approach i, although I have not checked which Polkit 0.105 variant the SailfishOS' version is based on or which backport patches it incorporates.

#### 1.2 

https://fossies.org/linux/libvirt/docs/auth.rst#unix-socket-policykit-auth