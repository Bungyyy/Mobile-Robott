;; Auto-generated. Do not edit!


(when (boundp 'ired_aruco::MPSPosition)
  (if (not (find-package "IRED_ARUCO"))
    (make-package "IRED_ARUCO"))
  (shadow 'MPSPosition (find-package "IRED_ARUCO")))
(unless (find-package "IRED_ARUCO::MPSPOSITION")
  (make-package "IRED_ARUCO::MPSPOSITION"))

(in-package "ROS")
;;//! \htmlinclude MPSPosition.msg.html


(defclass ired_aruco::MPSPosition
  :super ros::object
  :slots (_number_found _id _x _y _theta ))

(defmethod ired_aruco::MPSPosition
  (:init
   (&key
    ((:number_found __number_found) 0)
    ((:id __id) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:x __x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:y __y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:theta __theta) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _number_found (round __number_found))
   (setq _id __id)
   (setq _x __x)
   (setq _y __y)
   (setq _theta __theta)
   self)
  (:number_found
   (&optional __number_found)
   (if __number_found (setq _number_found __number_found)) _number_found)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:serialization-length
   ()
   (+
    ;; int16 _number_found
    2
    ;; string[] _id
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _id)) 4
    ;; float64[] _x
    (* 8    (length _x)) 4
    ;; float64[] _y
    (* 8    (length _y)) 4
    ;; float64[] _theta
    (* 8    (length _theta)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _number_found
       (write-word _number_found s)
     ;; string[] _id
     (write-long (length _id) s)
     (dolist (elem _id)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float64[] _x
     (write-long (length _x) s)
     (dotimes (i (length _x))
       (sys::poke (elt _x i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _y
     (write-long (length _y) s)
     (dotimes (i (length _y))
       (sys::poke (elt _y i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _theta
     (write-long (length _theta) s)
     (dotimes (i (length _theta))
       (sys::poke (elt _theta i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _number_found
     (setq _number_found (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; string[] _id
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _id (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _id i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float64[] _x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _x i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _y i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _theta
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _theta (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _theta i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get ired_aruco::MPSPosition :md5sum-) "769b8cad66706e9d423d19e4152250be")
(setf (get ired_aruco::MPSPosition :datatype-) "ired_aruco/MPSPosition")
(setf (get ired_aruco::MPSPosition :definition-)
      "int16 number_found
string[] id
float64[] x
float64[] y
float64[] theta
")



(provide :ired_aruco/MPSPosition "769b8cad66706e9d423d19e4152250be")


