
(cl:in-package :asdf)

(defsystem "ired_aruco-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MPSPosition" :depends-on ("_package_MPSPosition"))
    (:file "_package_MPSPosition" :depends-on ("_package"))
  ))