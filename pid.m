% Here the error function used in PID should be a function dependent on time
% But since the error function used in our PID algo is a Function dependent on the X-parameter(value from the read sensor)
% So The PID here is merely a st.line and function in linear of x and t.


% error=setpoint-presentvalue  where the present value is obtained from the read sensor function       
%Kp=210,Ki=0.2,Kd=100
%PID=kp*error+kd*error/t+ki*error*t
  
% Plot of PID with X keeping t=2s
x=[0:.1:5];
t=1;
kp=210;
ki=0.2;
kd=100;
PID=kp.*(3.0-x)+ki.*(3.0-x)*t+kd.*((3.0-x)/t);
subplot(2,2,1)
plot(x,PID,'--r','linewidth',2)
grid on
xlabel('x(sensor value)');
ylabel('PID');


% Plot of PID with t keeping X=3
t=[1:.1:10];
x=4;
kp=210;
ki=0.2;
kd=100;
PID=(kp*(3.0-x))+(ki*(3.0-x)).*t+(kd*(3.0-x))./t;
subplot(2,2,2)
plot(t,PID,'--b','linewidth',2)
grid on
xlabel('t(time)');
ylabel('PID');


% 3D-Plot of PID with t and X
t=[1:.1:5];
x=[1:.1:5];
kp=210;
ki=0.2;
kd=100;
PID=(kp.*(3.0-x))+(ki.*(3.0-x)).*t+(kd.*(3.0-x))./t;
subplot(2,2,3)
plot3(PID,x,t,'--k','linewidth',2)
grid on
xlabel('PID')
ylabel('x(sensorvalue)');
zlabel('time');
